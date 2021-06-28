import socket
import pickle

IP = "192.168.1.234"
PORT = 5555
ADDR = (IP, PORT)
BUFF_SIZE = 512

array1 = [1,2,3,4,5]
array2 = [2,3,4]

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Sending to the server...")

    array1_bytes = pickle.dumps(array1)
    array2_bytes = pickle.dumps(array2)
    server.sendto(array1_bytes, ADDR)
    server.sendto(array2_bytes, ADDR)

    result_bytes, addr = server.recvfrom(BUFF_SIZE)
    result = pickle.loads(result_bytes)
    print(f"Intersection: {result}")

