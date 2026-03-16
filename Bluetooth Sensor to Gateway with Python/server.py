import socket

# Add your Bluetooth MAC address here
HOST_MAC = "XX:XX:XX:XX:XX:XX"
PORT = 4

server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server_socket.bind((HOST_MAC, PORT))
server_socket.listen(1)

print("Waiting for Bluetooth client connection...")

connection, address = server_socket.accept()
print(f"Connected to: {address}")

try:
    while True:
        message = connection.recv(1024)
        if not message:
            break
        print("Received:", message.decode("utf-8"))

except OSError:
    pass

connection.close()
server_socket.close()
