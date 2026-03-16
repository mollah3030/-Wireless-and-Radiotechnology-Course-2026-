# Bluetooth Sensor to Gateway with Python

## Project Description
In this project, a simple Bluetooth client-server application is created in Python. The client simulates a sensor device that generates random temperature data every 5 seconds. This data is sent over Bluetooth to a gateway device (server), which receives and prints the data.

The client uses Bluetooth RFCOMM sockets to send temperature values (simulated by random data generation), and the server listens for incoming Bluetooth connections, receiving and printing the data.

## Bluetooth MAC Address Used
* **Server Address:** `00:00:00:00:00:00` (Replace with your actual Bluetooth MAC address)
