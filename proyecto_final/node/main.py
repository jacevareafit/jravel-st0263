import grpc
import files_pb2
import files_pb2_grpc

import os
from concurrent import futures
from os.path import isfile, join
from os import listdir

class Files(files_pb2_grpc.FilesServicer):
    def PingFiles(self, request, context):
        response = files_pb2.PingFilesResponse(ack='1')
        return response
    def ListFiles(self, request, context):
        try:
            files = [f for f in listdir("src/") if isfile(join("src/", f))]
            response = files_pb2.ListFilesResponse(files=files,status=200)
        except:
            response = files_pb2.ListFilesResponse(status=500)
        return response
    def DownloadFile(self, request, context):
        chunk_size = 1024

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

        for request in request_iterator:
            if request.fileName:
                filepath += request.fileName
                continue
            data.extend(request.chunk_data)
        with open(filepath, 'wb') as f:
            f.write(data)
        return files_pb2.EmptyMessage()

def createServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2), 
        options = [
            ('grpc.max_send_message_length', 16772984),
            ('grpc.max_receive_message_length', 16772984)
        ]
    )

    files_pb2_grpc.add_FilesServicer_to_server(Files(),server)

    port = 50051
    server.add_insecure_port('[::]:'+str(port))
    server.start()
    print("server started, port: "+str(port))
    server.wait_for_termination()

def main():
    createServer()
    # print(listFiles())
    

if __name__ == "__main__":
    main()