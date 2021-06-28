import socket
import pickle

HOST = "127.0.0.1"
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)

while True:
    conn, addr = s.accept()
    print("Client connected with address " + str(addr))
    buff = conn.recv(100)
    arr = pickle.loads(buff)
    print("Summing " + str(arr))

    result = sum(arr)
    conn.send(pickle.dumps(result))
