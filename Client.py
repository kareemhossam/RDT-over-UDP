from socket import *
from sys import argv

SEGMENT_SIZE = 100

if __name__ == '__main__':

    if len(argv) == 1:
        print('Will use stop and wait by default, otherwise USAGE: '
              'python3 Client.py <1:Stop and Wait, 2:Selective repeat, '
              '3: Go Back N>')
    protocol = argv[1]

    serverName = 'localhost'
    PortSend = 12000
    PortRecv = 12001
    listen = (serverName, PortRecv)
    dest = (serverName, PortSend)

    send_sock = socket(AF_INET, SOCK_DGRAM)
    recv_sock = socket(AF_INET, SOCK_DGRAM)

    recv_sock.bind(listen)
    recv_sock.settimeout(1)

    offset = 0
    seq = 0

    with open('payload.txt') as f:
        content = f.read()

    while offset < len(content):
        if offset + SEGMENT_SIZE > len(content):
            segment = content[offset:]
        else:
            segment = content[offset:offset + SEGMENT_SIZE]
        offset += SEGMENT_SIZE

        ack_received = False
        while not ack_received:
            send_sock.sendto(str(seq) + segment, dest)
            try:
                message, address = recv_sock.recvfrom(4096)
            except timeout:
                print("Timeout")
            else:
                print(message)
                ack_seq = message[3]
                if ack_seq == str(seq):  # assuming max number of ACKs is 10
                    ack_received = True
        seq = 1 - seq
