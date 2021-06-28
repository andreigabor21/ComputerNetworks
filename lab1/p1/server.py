import socket
import struct
import pickle

port = 1234
host = "127.0.0.1"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
s.bind((host, port))
print("Binded")
s.listen(5)
con, addr = s.accept()
print("Connection accepted")

len = con.recv(2)
len = struct.unpack('!H', len)[0]
lst = []
for i in range(len):
    elem = con.recv(2)
    elem = struct.unpack('!H', elem)[0]
    lst.append(elem)
suma = sum(lst)
print(suma)

suma = struct.pack('!H', suma)
con.send(suma)
con.close()
