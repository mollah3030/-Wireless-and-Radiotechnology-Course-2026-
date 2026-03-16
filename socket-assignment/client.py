import socket
import random
import time

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")

    while True:
        temp_value = round(random.uniform(20.0, 35.0), 1)
        message = f"Temperature: {temp_value} C"

        client.send(message.encode("utf-8"))
        print("Sent:", message)

        time.sleep(5)

except ConnectionRefusedError:
    print("Could not connect to the server. Make sure server.py is running first.")

except KeyboardInterrupt:
    print("\nClient stopped.")

finally:
    client.close()
    print("Client socket closed.")
