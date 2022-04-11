import socket
import json

content_names = dict()

serverFormat = "utf-8"
serverPort = 5001

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

serverSocket.bind( ('', serverPort) )
print("UDP server is ready to receive")

def PrepareChunkJSON(ip,files):
    for file in files:
        if file in content_names.keys():
            if ip not in content_names[file]:
                content_names[file].append(ip)
        else:
            content_names[file] = [ip]

while 1:
    msg, addr = serverSocket.recvfrom(1024)
    decoded_msg = msg.decode(serverFormat)

    python_dict = json.loads(decoded_msg)
    ip = addr[0]
    files = python_dict["chunks"]

    PrepareChunkJSON(ip,files)
    
    print(content_names)
    
    with open('chunks.json','w') as file:
        file.write(json.dumps(content_names))

    print("Discovered all contents")