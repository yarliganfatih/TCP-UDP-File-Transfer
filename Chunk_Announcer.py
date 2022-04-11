import os
import math
import socket
import json
import time

if not (os.path.exists('Chunks/')):
    os.mkdir('Chunks/')

def Prepare_Chunk(file_path, file_extention):
    filename = file_path+'.'+file_extention
    c = os.path.getsize(filename)
    CHUNK_SIZE = math.ceil(math.ceil(c)/5)
    index = 1
    with open(filename, 'rb') as infile:
        chunk = infile.read(int(CHUNK_SIZE))
        while chunk:
            chunkname = file_path+'_'+str(index)
            with open("Chunks/"+chunkname,'wb+') as chunk_file:
                chunk_file.write(chunk)
            index += 1
            chunk = infile.read(int(CHUNK_SIZE))
    print("Chunks are ready.")
    chunk_file.close()

serverFormat = "utf-8"
serverIP = 'localhost'
serverPort = 5001
server_address = (serverIP, serverPort)
hamachi_adress = ("25.255.255.255", serverPort)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

def Announcer():

    path = os.getcwd() + "/" + "Chunks"
    files = os.listdir(path)
    python_dict = {"chunks" : files}
    json_dict = json.dumps(python_dict)
    print("Announcing..")
    clientSocket.sendto(json_dict.encode(serverFormat), hamachi_adress) #server_address
    
def main():
    file_name = input("File content name : ")
    file_extention = input("File extention : ")
    Prepare_Chunk(file_name, file_extention)
    while 1:
        Announcer()
        time.sleep(15)
        print("Successfull")

main()