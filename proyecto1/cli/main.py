import grpc
import files_pb2
import files_pb2_grpc

import os
from concurrent import futures
import requests
import re
from dotenv import load_dotenv


class CLIInterface:
    def __init__(self, name_node_url):
        self.name_node_url = name_node_url

    def interactuar_cli(self):
        print("Bienvenido al sistema de archivos distribuidos")
        print("Seleccione una opción:")
        print("1. GET")
        print("2. PUT")
        print("3. SEARCH")
        print("4. LIST")
        eleccion_usuario = input("Ingrese el número de su elección: ")

        if eleccion_usuario == "1":
            self.get_file(input("Ingrese el nombre del archivo: "))
        elif eleccion_usuario == "2":
            self.put_file(input("Ruta del archivo: "))
        elif eleccion_usuario == "3":
            self.search_files(input("Ingrese la expresión regular: "))
        elif eleccion_usuario == "4":
            self.list_files()
        else:
            print("Opción inválida. Intente de nuevo.")
            self.interactuar_cli()

    def get_file(self, file_name):
        try:
            dataNode = ""
            with grpc.insecure_channel(self.name_node_url) as chan:
                stub = files_pb2_grpc.FilesStub(chan)
                response = stub.NamenodeDownloadFile(files_pb2.DownloadFileRequest(fileName=file_name))
                if response.status == 200:
                    dataNode = response.conn
                else:
                    print("Error: No se pudo obtener el archivo")
                    return
            
            with grpc.insecure_channel(dataNode) as chan:
                stub = files_pb2_grpc.FilesStub(chan)
                filepath = "src/"+file_name
                for entry_response in stub.DownloadFile(files_pb2.DownloadFileRequest(fileName=file_name)):
                    with open(filepath, mode="ab") as f:
                        f.write(entry_response.chunk_data)
                        f.close()
            print("New file: "+file_name)
        except:
            print("Error: No se pudo obtener el archivo")

    def read_iterfile(self,filepath, chunk_size=1024):
        _, filename = os.path.split(filepath)
        yield files_pb2.UploadFileRequest(fileName=filename)
        with open(filepath, mode="rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if chunk:
                    entry_request = files_pb2.UploadFileRequest(chunk_data=chunk)
                    yield entry_request
                else: # end of file
                    return         

    def put_file(self, file_path):
        try:
            dataNode = ""
            with grpc.insecure_channel(self.name_node_url) as chan:
                stub = files_pb2_grpc.FilesStub(chan)
                response = stub.NamenodeUploadFile(files_pb2.EmptyMessage())
                if response.status == 200:
                    dataNode = response.conn
                else:
                    print("Error: No se pudo subir el archivo")
                    print("Fallo namenode")
                    return
            with grpc.insecure_channel(dataNode) as chan:
                stub = files_pb2_grpc.FilesStub(chan)
                stub.UploadFile(self.read_iterfile(file_path))
            print("File upload")
        except:
            print("Error: No se pudo subir el archivo")

    def search_files(self, regex):
        with grpc.insecure_channel(self.name_node_url) as chan:
            stub = files_pb2_grpc.FilesStub(chan)
            response = stub.SearchFiles(files_pb2.SearchFilesRequest(regex=regex))
            if response.status == 200:
                print(response.files)
            else:
                print("Error: No se pudo realizar la búsqueda")


    def list_files(self):
        with grpc.insecure_channel(self.name_node_url) as chan:
            stub = files_pb2_grpc.FilesStub(chan)
            request = files_pb2.EmptyMessage()
            response = stub.ListFiles(request)

        # response = requests.get(self.name_node_url  + '/list')
        if response.status == 200:
            print(response.files)
        else:
            print("Error: No se pudo listar los archivos")
            print("Status code: ", response.status)


if __name__ == "__main__":
    load_dotenv()
    namenode = str(os.getenv("namenode")).encode('utf-8')
    print(namenode)
    cli = CLIInterface(namenode)
    cli.interactuar_cli()