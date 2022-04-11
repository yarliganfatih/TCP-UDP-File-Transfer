import socket
import json
import datetime
import time

# Log_Downloads
def saveLogs(ip, chunkname):
    file = open("Log_Uploads.txt","a")
    file.write(str(time.time())+" "+ip+" "+chunkname+"\n")
    file.close()

serverFormat = "utf-8"
serverIP = "localhost"
#print(serverIP)
serverPort = 8000
server_address = ('', serverPort)
c = 0

serverSocket = socket.socket()
serverSocket.bind( (serverIP, serverPort) )
serverSocket.listen(5)
print("TCP server is ready to receive")
while 1:
    c,address = serverSocket.accept()
    print("Connection established with " + address[0])
    msg = c.recv(1024)
    data = msg.decode(serverFormat)
    data = json.loads(data)
    #print(data)
    image = open("Chunks/"+data["requested_content"],"rb")
    if c != 0:
        for i in image:
            c.send(i)
    print(data["requested_content"]+" uploaded")
    saveLogs(address[0], data["requested_content"])
    c.close()