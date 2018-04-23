from socket import *
'''import numpy as np

max_packet_length = 500

class Packet:
    cksum = np.uint16(None)
    length = np.uint16(None)
    seqno = np.uint16(None)
    data = "\0" * (max_packet_length -8)

class ack_packet:
    cksum = np.uint16(None)
    length = np.uint16(None)
    ackno = np.uint16(None)

def get_arg(max,seed,p):
'''
#this is a test 
serverName = 'hostname'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input lowercase sentence:")
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
