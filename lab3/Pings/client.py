import socket
import sys
import time

FORMAT = 'utf-8'
BUF_SIZE = 1024
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (sys.argv[1], int(sys.argv[2]))
while True:
    message = str(list(range(1, 10)))

    begin = time.time()
    udp_socket.sendto(message.encode(FORMAT), server_address)
    received, addr = udp_socket.recvfrom(BUF_SIZE)
    end = time.time()

    received_message = received.decode(FORMAT)
    if message == received_message:
        print("Same message")
    else:
        print("{0} differs from {1}".format(message, received_message))
    print("It took {0} seconds".format(end - begin))
    time.sleep(1)
