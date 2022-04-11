import socket
import datetime
import time
import json
import os


if not (os.path.exists('Chunks/')):
    os.mkdir('Chunks/')

if not (os.path.exists('Downloaded_Chunks/')):
    os.mkdir('Downloaded_Chunks/')
    
if not (os.path.exists('Downloads/')):
    os.mkdir('Downloads/')

contentNames = []
request_content = dict()

serverPort = 8000

# Log_Downloads
def saveLogs(ip, chunkname):
    file = open("Log_Downloads.txt","a")
    file.write(str(time.time())+" "+ip+" "+chunkname+"\n")
    file.close()

# from Content_Discovery.py
def getContents():
    with open('chunks.json','r') as file:
        contents = json.load(file)

    for key in contents.keys():
        content = key.split('_')[0]

        if content not in contentNames:
            contentNames.append(content)
        
    return contents

# get chunks
def getChunks(jsonMsg,chunkName,serverSocket):

    if chunkName not in contents.keys():
        serverSocket.close()
        return 0,"NoN"
    
    ippAddr = contents[chunkName]
    
    print(chunkName)
    for ip in ippAddr:
        if Connect(ip,serverSocket):

            serverSocket.send(jsonMsg.encode())
            while 1:
                chunk = serverSocket.recv(1024)
                if len(chunk) <= 0:
                    serverSocket.close()
                    break
                
                chunkPath = "Downloaded_Chunks/" + chunkName
                with open(chunkPath,'ab+') as infile:
                    infile.write(chunk)
                
            return 1, ip
    
    return 1,"NoN"

# Try cacth
def Connect(ip,serverSocket):
    try:
        serverSocket.connect((ip,serverPort))
        print(f"Connection established with {ip}.")
        return 1
    except:
        print(f'Connection do not established with {ip}.')
        return 0

# Combine Chunks
def CombineChunks(chunkName,chunkNames):
    with open('Downloads/'+chunkName+'.png', 'wb') as outfile:
        for chunk in chunkNames: 
            with open('Downloaded_Chunks/'+chunk, 'rb') as infile: 
                outfile.write(infile.read() )
            infile.close()
            
# ready for P2P
def replaceChunks(chunkNames):
    for chunk in chunkNames:
        os.replace("Downloaded_Chunks/" + chunk,"Chunks/" + chunk)

while 1:
    contents = getContents()

    print("Contents in the network : ")
    for content in contentNames:
        print(content)

    contentName = input('Enter the file name you want to download (no extention) : ')

    chunkNames = []
    for cn in range(1,6):
        serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        chunkName = contentName + '_' + str(cn)

        request_content['requested_content'] = chunkName
        jsonMsg = json.dumps(request_content)
        
        success,ip = getChunks(jsonMsg,chunkName,serverSocket)

        if success:
            chunkNames.append(chunkName)
            saveLogs(ip,chunkName)
        else:
            serverSocket.close()
            print(chunkName + " download is unsuccessful")

    if len(chunkNames) >= 5:
        CombineChunks(contentName,chunkNames)
        print("All chunks have been downloaded and merged successfully")  
    
    replaceChunks(chunkNames)