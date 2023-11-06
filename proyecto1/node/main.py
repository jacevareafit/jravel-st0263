import grpc
import files_pb2
import files_pb2_grpc

from dotenv import load_dotenv
import os
from concurrent import futures
from os.path import isfile, join
from os import listdir

def listFiles():
    files = [f for f in listdir("src/") if isfile(join("src/", f))]
    return files

class Files(files_pb2_grpc.FilesServicer):
    def PingFiles(self, request, context):
        response = files_pb2.PingFilesResponse(ack='1')
        return response
    def ListFiles(self, request, context):
        try:
            files = listFiles()
            print("ListFiles Request")
            response = files_pb2.ListFilesResponse(files=files,status=200)
        except:
            response = files_pb2.ListFilesResponse(status=500)
        return response
    def DownloadFile(self, request, context):
        chunk_size = 1024
        print("Download Request")
        filepath = "src/"+request.fileName
        if os.path.exists(filepath):
            print("Sending: "+filepath)
            with open(filepath, mode="rb") as f:
                while True:
                    chunk = f.read(chunk_size)
                    if chunk:
                        entry_response = files_pb2.DownloadFileResponse(chunk_data=chunk)
                        yield entry_response
                    else:
                        return
    
    def UploadFile(self, request_iterator, context):
        data = bytearray()
        filepath = 'src/'
        print("UPLOAD Request")

        for request in request_iterator:
            if request.fileName:
                filepath += request.fileName
                print("Uploading: "+request.fileName)
                continue
            data.extend(request.chunk_data)
        with open(filepath, 'wb') as f:
            f.write(data)
        
        namenode = os.getenv("namenode")
        datanode = os.getenv("datanode")
        with grpc.insecure_channel(namenode) as chan:
            stub = files_pb2_grpc.FilesStub(chan)
            request = files_pb2.NameNodeRequest(conn=datanode,files=listFiles())
            response = stub.NamenodeConn(request)
            if response.status == 200:
                print("Namenode success!")
        
        return files_pb2.EmptyMessage()

def createServer():
    namenode = os.getenv("namenode")
    print("namenode", namenode)
    datanode = os.getenv("datanode")
    with grpc.insecure_channel(namenode) as chan:
        stub = files_pb2_grpc.FilesStub(chan)
        request = files_pb2.NameNodeRequest(conn=datanode,files=listFiles())
        response = stub.NamenodeConn(request)
        if response.status == 200:
            print("Namenode success!")

    server = grpc.server(futures.ThreadPoolExecutor())

    files_pb2_grpc.add_FilesServicer_to_server(Files(),server)

    port = 50051
    server.add_insecure_port('[::]:'+str(port))
    server.start()
    print("server started, port: "+str(port))
    server.wait_for_termination()

def main():
    load_dotenv()
    createServer()    

if __name__ == "__main__":
    main()