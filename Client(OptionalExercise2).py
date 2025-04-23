import socket
import sys

if len(sys.argv) != 4:
    print("Usage: python Client(OptionalExercise2).py <server_host> <server_port> <filename>")
    sys.exit(1)

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientSocket.connect((server_host, server_port))

    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    print(f"Sending request:\n{request}")

    clientSocket.send(request.encode())

    response = b""
    while True:
        chunk = clientSocket.recv(4096)
        if not chunk:
            break
        response += chunk

    print("Response from server:\n")
    print(response.decode(errors="ignore"))

finally:
    clientSocket.close()
