from socket import *
import os

#mybranch
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(4)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
    print(modifiedMessage.decode('ascii'))
'''
    print('recieving message')
    print('recieved {0} bytes from ${1}'.format(len(modifiedMessage), clientAddress))
    print('the message is:'+ modifiedMessage.decode('ascii'))
    if modifiedMessage:
    	sent=serverSocket.sendto(modifiedMessage, clientAddress)
    	print('{0} bytes are sent back to the client {1}'.format(sent,clientAddress))
'''
