import grpc
import files_pb2
import files_pb2_grpc

import random
import os
from concurrent import futures
import requests
import re

nodes = []
files = {}

class Files(files_pb2_grpc.FilesServicer):
    def NamenodeConn(self, request, context):
        print("DataNode request")
        if request.conn:
            nodes.append(request.conn)
            files[request.conn] = request.files
            print("-- Connecction: "+request.conn)

        return files_pb2.StatusMessage(status=200)

    def ListFiles(self, request, context):
        print("LIST Request")
        listFiles = []
        for i in files:
            for file in files[i]:
                listFiles.append(file)
        print(listFiles)
        return files_pb2.ListFilesResponse(files=listFiles,status=200)
    
    def NamenodeDownloadFile(self, request, context):
        fileName = request.fileName
        for i in files:
            for file in files[i]:
                if file == fileName:
                    return files_pb2.DataNodeResponse(conn=i,status=200)
        return files_pb2.DataNodeResponse(status=400)
    
    def NamenodeUploadFile(self, request, context):
        if len(nodes)==0:
            return files_pb2.DataNodeResponse(status=400)

        node = nodes[random.randrange(len(nodes))]
        return files_pb2.DataNodeResponse(conn=node,status=200)
    
    def SearchFiles(self, request, context):
        regex = re.compile(request.regex)
        listFiles = []
        for i in files:
            for file in files[i]:
                listFiles.append(file)
        filtered_list = [item for item in listFiles if regex.search(item)]
        return files_pb2.ListFilesResponse(files=filtered_list,status=200)
    
def createServer():
    server = grpc.server(futures.ThreadPoolExecutor())

    files_pb2_grpc.add_FilesServicer_to_server(Files(),server)

    port = 50050
    server.add_insecure_port('[::]:'+str(port))
    server.start()
    print("server started, port: "+str(port))
    server.wait_for_termination()

def main():
    createServer()
    # print(listFiles())
    

if __name__ == "__main__":
    main()