import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server is listening on {HOST}:{PORT}")

client_socket, client_address = server.accept()
print(f"Connected by {client_address}")

try:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        print("Received:", data.decode("utf-8"))

except KeyboardInterrupt:
    print("\nServer stopped.")

finally:
    client_socket.close()
    server.close()
    print("Server socket closed.")
