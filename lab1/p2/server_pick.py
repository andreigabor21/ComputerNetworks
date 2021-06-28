import socket
import threading
import pickle

HEADER = 64
PORT = 5050
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn: socket.socket, addr):
    print(f"New connection from {addr}")
    buffer = conn.recv(HEADER)
    message = pickle.loads(buffer)
    print(message)
    spaces = count_spaces(message)
    conn.send(pickle.dumps(spaces))

def count_spaces(string: str) -> int:
    count = 0
    for character in string:
        if character == " ":
            count += 1
    return count


def start_server():
    server.listen()
    print(f"Server is listening on {ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == '__main__':
    print("Server is starting...")
    start_server()