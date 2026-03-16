# Bluetooth Sensor to Gateway with Python

## Project Description

In this project, a simple Bluetooth client-server application is created in Python. The client simulates a sensor device that generates random temperature data every 5 seconds. This data is sent over Bluetooth to a gateway device (server), which receives and prints the data.

The client uses Bluetooth RFCOMM sockets to send temperature values (simulated by random data generation), and the server listens for incoming Bluetooth connections, receiving and printing the data.

## Bluetooth MAC Address Used

* **Server (Gateway) Bluetooth MAC address:** XX:XX:XX:XX:XX:XX
*(Replace this with your actual MAC address)*

## How to Run

### Step 1: Setup Bluetooth on both devices

* Ensure Bluetooth is enabled on both devices (client and server).
* Pair the devices via Bluetooth.
* Find the Bluetooth MAC address of the server device.

### Step 2: Running the Server

1. Run the `server.py` on the gateway device.
   ```bash
   python server.py
