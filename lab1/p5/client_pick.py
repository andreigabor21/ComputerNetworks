import pickle
import socket

BUFSIZE = 64
IP = "192.168.56.1"
PORT = 5050
ADDR = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(n: int):
    numberInBytes = pickle.dumps(n)
    client.send(numberInBytes)
    listBytes = client.recv(BUFSIZE)
    print(pickle.loads(listBytes))

if __name__ == '__main__':
    while True:
        n = int(input("Read the number>>"))
        send(n)
        if n == 0:
            break
    client.close()