import socket
import threading

IP = "0.0.0.0"
PORT = 1234
ADDR = (IP, PORT)
BUF_SIZE = 1024
FORMAT = 'utf-8'

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(ADDR)
print("UDP Server started")

def worker(message: str, addr):
    print("Message: {0} from {1}\n", message, addr)
    copy_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    copy_socket.sendto(message.encode(FORMAT), addr)

if __name__ == '__main__':
    while True:
        message, addr = udp_socket.recvfrom(BUF_SIZE)
        message = message.decode(FORMAT)
        thread = threading.Thread(target=worker, args=(message, addr))
        thread.start()