import pickle
import socket
import threading

BUFSIZE = 64
PORT = 5050
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def divisors(n: int) -> list:
    res = []
    for i in range(2, n//2+1):
        if n % i == 0:
            res.append(i)
    return res

def handle_client(conn: socket.socket, addr):
    print(f"Active connections: {threading.activeCount() - 1}")
    connected = True
    while connected:
        n = conn.recv(BUFSIZE)
        if n:
            n = pickle.loads(n)
            if n == 0:
                connected = False
            divs = divisors(n)
            conn.send(pickle.dumps(divs))
    print(f"Client {addr} disconnected")
    conn.close()

def start():
    server.listen()
    print(f"Server is listening on {IP}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == '__main__':
    print("Server is starting...")
    start()