import pyodbc
import socket
from threading import Thread

FORMAT = "utf-8"
IP = "192.168.1.234"
PORT = 5050
ADDR = (IP, PORT)

class ClientThread(Thread):

    def __init__(self, conn: socket.socket, ip, port):
        Thread.__init__(self)
        self.conn = conn
        self.ip = ip
        self.port = port

    def getBooks(self):
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                              'Server=DESKTOP-C0SCI39;'
                              'Database=BookLibrary;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('SELECT *'
                       'FROM Books')
        books = ""
        for row in cursor:
            books += row[5] + " - " + row[8] + '\n'
        return books

    def run(self):
        booksString = self.getBooks()
        self.conn.send(booksString.encode(FORMAT))

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
    server.bind(ADDR)
    server.listen()
    print(f"Server is listening on {IP}")

    threads = []
    while True:
        (conn,(ip, port)) = server.accept()
        print(f"Client with IP {ip} connected")
        clientWorker = ClientThread(conn, ip, port)
        clientWorker.run()
        threads.append(clientWorker)
    for thread in threads:
        thread.join()
