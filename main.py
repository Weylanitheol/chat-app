import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        print(f"Received message: {message}")
        client_socket.sendall(f"Server received: {message}".encode('utf-8'))
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8888))
server_socket.listen(5)

print("Server listening on port 8888")

while True:
    client, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
