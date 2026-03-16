import socket
import random
import time

# Put the Bluetooth MAC address of the server here
SERVER_MAC = "XX:XX:XX:XX:XX:XX"
PORT = 4

client_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client_socket.connect((SERVER_MAC, PORT))

print("Connected to Bluetooth server")

try:
    while True:
        # Create a random temperature value between 20.0 and 30.0
        temp_value = round(random.uniform(20.0, 30.0), 1)
        data = f"Temperature: {temp_value} C"

        # Send data to the server
        client_socket.send(data.encode("utf-8"))
        print("Sent:", data)

        # Wait 5 seconds before sending again
        time.sleep(5)

except OSError:
    pass

client_socket.close()
