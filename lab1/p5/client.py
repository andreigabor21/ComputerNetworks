import pickle
import struct
import socket

BUFSIZE = 64
IP = "192.168.56.1"
PORT = 2020
ADDR = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(n: int):
    numberInBytes = struct.pack("!H", n)
    client.send(numberInBytes)

    length = client.recv(BUFSIZE)
    length = struct.unpack("!H", length)[0]
    capture = []
    for i in range(length):
        bytesElem = client.recv(2)
        capture.append(struct.unpack("!H", bytesElem)[0])
    print(capture)

if __name__ == '__main__':
    while True:
        n = int(input("Read the number>>"))
        send(n)
        if n == 0:
            break
    client.close()