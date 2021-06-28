import socket
import struct

host = "127.0.0.1"
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

lista = [1,2,3,4]
length = len(lista)
s.send(struct.pack('!H', length))

for i in range(len(lista)):
    s.send(struct.pack('!H', lista[i]))

suma = s.recv(2)
suma = struct.unpack('!H', suma)[0]
print(suma)
s.close()
