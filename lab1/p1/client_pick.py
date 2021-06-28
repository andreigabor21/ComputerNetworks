import socket
import pickle

HOST = "127.0.0.1"
PORT = 1234

array = [1, 2, 3, 4]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Client sending the array to the server")

arrayAsBytes = pickle.dumps(array)
s.send(arrayAsBytes)

sum_array = s.recv(100)

print("Sum received: ")
print(pickle.loads(sum_array))
