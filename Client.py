from socket import *

#my branch
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:').encode('ascii')
l = len(message)
print(l)
i = 0
while i < l:
    clientSocket.sendto(message[i:i+4], (serverName, serverPort))
    i += 4
    modifiedMessage, serverAddress = clientSocket.recvfrom(4)
    print(modifiedMessage.decode('ascii'))

# clientSocket.sendto(message, (serverName, serverPort))
clientSocket.close()
