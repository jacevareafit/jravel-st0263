import grpc
import files_pb2
import files_pb2_grpc

import os
from concurrent import futures
import requests
import re

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

    def _get_data_node_url(self, action, file_name=None):
        #payload = {'action': action, 'file_name': file_name}
        #response = requests.get(self.name_node_url, params=payload)
        #if response.status_code == 200:
        #    return response.text
        #else:
        #    print("Error: No se pudo obtener la URL del DataNode")
        #    self.interactuar_cli()
        return "127.0.0.1:50051"

    def get_file(self, file_name):
        try:
            data_node_url = self._get_data_node_url('GET', file_name)
            with grpc.insecure_channel(data_node_url) as chan:
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
        # _, filename = os.path.split(filepath)
        yield files_pb2.UploadFileRequest(fileName="src/testUpload.txt")
        with open(filepath, mode="rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if chunk:
                    entry_request = files_pb2.UploadFileRequest(chunk_data=chunk)
                    yield entry_request
                else: # end of file
                    return
                

    def put_file(self, file_path):
        data_node_url = self._get_data_node_url('PUT')
        with grpc.insecure_channel("localhost:50051") as chan:
            stub = files_pb2_grpc.FilesStub(chan)
            stub.UploadFile(self.read_iterfile(file_path))
        
        print("Error: No se pudo subir el archivo")

    def search_files(self, regex):
        response = requests.get(self.name_node_url  + '/search', params={'regex': regex})
        if response.status_code == 200:
            matches = re.findall(regex, response.text)
            print(matches)
        else:
            print("Error: No se pudo realizar la búsqueda")
            print("Status code: ", response.status_code)


    def list_files(self):
        # No se deberia hacer contra un nodo sino con el namenode
        ip = "127.0.0.1"
        port = "50051"
        with grpc.insecure_channel(ip+":"+str(port)) as chan:
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
    cli = CLIInterface("http://namenode_url")
    cli.interactuar_cli()

#def main():
#    ip = "127.0.0.1"
#    port = "50051"
#    with grpc.insecure_channel(ip+":"+str(port)) as chan:
#        stub = files_pb2_grpc.FilesStub(chan)
        
        # list files
        # request = files_pb2.EmptyMessage()
        # result = stub.ListFiles(request)
        # print(f'result:{result.files}')


        # download file
        # filepath = "src/file1.txt"
        # for entry_response in stub.DownloadFile(files_pb2.DownloadFileRequest(fileName="file1.txt")):
        #    with open(filepath, mode="ab") as f:
        #        f.write(entry_response.chunk_data)
        #        f.close()

        # upload file
#        stub.UploadFile(read_iterfile('test.txt'))

    

#if __name__ == "__main__":
#    main()