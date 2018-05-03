from socket import *

#my branch
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
choose =int(input('1:stop and wait \n2:Go back N\n3:selective repeate \nchoose sending method: '))
message = input('Input lowercase sentence:').encode()
l = len(message)
print(l)
i = 0
if( choose == 1):
    window=1
    while i < l:
        clientSocket.sendto(message[i:i+window], (serverName, serverPort))
        i += window
        modifiedMessage, serverAddress = clientSocket.recvfrom(window)
        #print(modifiedMessage.decode('ascii'))

        #clientSocket.sendto(message, (serverName, serverPort))
    clientSocket.close()
elif(choose == 2):
    window=int(input('please choose the window size:'))
    while i < l:
        clientSocket.sendto(message[i:i+window], (serverName, serverPort))
        i += window
        modifiedMessage, serverAddress = clientSocket.recvfrom(window)
        #print(modifiedMessage.decode('ascii'))

        # clientSocket.sendto(message, (serverName, serverPort))
    clientSocket.close()

elif(choose == 3):
    window=int(input('please choose the window size:'))
    while i < l:
        clientSocket.sendto(message[i:i+window], (serverName, serverPort))
        i += window
        modifiedMessage, serverAddress = clientSocket.recvfrom(window)
        #print(modifiedMessage.decode('ascii'))

        # clientSocket.sendto(message, (serverName, serverPort))
    clientSocket.close()

else:
    print("invalid choice")
