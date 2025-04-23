# import socket module
import threading
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12001
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
def handle_client(connectionSocket,adr):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:], "r")
        outputdata = f.read()
        f.close()

        responseHeader = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(responseHeader.encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())

    except IOError:
        responseHeader = "HTTP/1.1 404 Not Found\r\n\r\n"
        responseBody = "<html><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send(responseHeader.encode() + responseBody.encode())

    finally:
        connectionSocket.close()
while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"New connection from {addr}")
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    client_thread.start()