import socket
import pickle

def intersection(first, second):
    res = []
    for n in first:
        if n in second:
            res.append(n)
    return res

IP = "0.0.0.0"
PORT = 5555
ADDR = (IP, PORT)
BUFF_SIZE = 512

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket created")
    sock.bind(ADDR)
    print("Waiting to receive...")

    buffer, addr = sock.recvfrom(BUFF_SIZE)
    array1 = pickle.loads(buffer)
    buffer, addr = sock.recvfrom(BUFF_SIZE)
    array2 = pickle.loads(buffer)

    res_bytes = pickle.dumps(intersection(array1, array2))
    sock.sendto(res_bytes, addr)

