from socket import *
from sys import argv, stdout

if __name__ == '__main__':

    if len(argv) == 1:
        print('Will use stop and wait by default, otherwise USAGE: '
              'python3 Server.py <1:Stop and Wait, 2:Selective repeat, '
              '3: Go Back N>')
    else:
        protocol = argv[1]

    # Socket Parameters:

    serverName = 'localhost'
    PortSend = 12001
    PortRecv = 12000

    # Tuple to save time for receiving Socket and sending Socket
    listen = (serverName, PortRecv)
    dest = (serverName, PortSend)

    # 2 Sockets one to send and one to receive
    send_sock = socket(AF_INET, SOCK_DGRAM)
    recv_sock = socket(AF_INET, SOCK_DGRAM)

    # initializing Receive Socket
    recv_sock.bind(listen)

    # initializing Sequence for receiving
    expecting_seq = 0

    while True:
        # Start Receiving
        message, address = recv_sock.recvfrom(4096)
        message = message.decode()
        # Extract Seq and Content from received message
        seq = message[0]
        content = message[1:]

        # Send Acknowledgment to Client
        ack_message = 'Ack' + seq
        send_sock.sendto(ack_message.encode(), dest)

        # if the received sequence number is the expected sequence number
        # besara7a el 7eta de msh mgama3ha awy fa 7awel tefhamha enta
        if seq == str(expecting_seq):
            # Print the Content and
            stdout.write(content)
            expecting_seq = 1 - expecting_seq
        else:
            negative_seq = str(1 - expecting_seq)
            ack_message = 'Ack' + negative_seq
            send_sock.sendto(ack_message.encode(), dest)
