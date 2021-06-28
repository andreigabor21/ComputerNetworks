import socket
import pickle

FORMAT = "utf-8"
HEADER = 64
IP = "192.168.56.1"
PORT = 5050
ADDR = (IP ,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(message: str):
    messageBytes = message.encode(FORMAT)
    client.send(messageBytes)


if __name__ == '__main__':
    string = input("Read a string>>")
    send(string)
    received = client.recv(HEADER)
    spaces = int(received.decode(FORMAT))
    print(f"String \"{string}\" contains {spaces} spaces")
    client.close()
