from socket import *
from sys import argv, stdout

if __name__ == '__main__':

    if len(argv) == 1:
        print('Will use stop and wait by default, otherwise USAGE: '
              'python3 Server.py <1:Stop and Wait, 2:Selective repeat, '
              '3: Go Back N>')
    protocol = argv[1]

    serverName = 'localhost'
    PortSend = 12001
    PortRecv = 12000
    listen = (serverName, PortRecv)
    dest = (serverName, PortSend)

    send_sock = socket(AF_INET, SOCK_DGRAM)
    recv_sock = socket(AF_INET, SOCK_DGRAM)

    recv_sock.bind(listen)

    expecting_seq = 0

    while True:
        message, address = recv_sock.recvfrom(4096)

        seq = message[0]
        content = message[1:]

        send_sock.sendto('Ack' + seq, dest)
        if seq == str(expecting_seq):
            stdout.write(content)
            expecting_seq = 1 - expecting_seq
        else:
            negative_seq = str(1 - expecting_seq)
            send_sock.sendto('ACK' + negative_seq, dest)
