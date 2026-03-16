# Bluetooth Sensor to Gateway with Python

## Project Description

This project demonstrates a basic Bluetooth client-server program written in Python. The client behaves like a sensor device and produces random temperature values every 5 seconds. These values are transmitted through Bluetooth to a gateway device, which acts as the server and receives and displays the data.

The client uses Bluetooth RFCOMM sockets to send the temperature readings, which are generated randomly to simulate sensor data. The server waits for incoming Bluetooth connections, receives the transmitted data, and prints it.

## Bluetooth MAC Address Used

- **Server (Gateway) Bluetooth MAC address:** `XX:XX:XX:XX:XX:XX`  
  *(Replace this with your real MAC address.)*

## How to Run

### Step 1: Setup Bluetooth on both devices

- Make sure Bluetooth is turned on for both the client and the server devices.
- Pair the two devices using Bluetooth.
- Find the Bluetooth MAC address of the server device.

### Step 2: Running the Server

Run `server.py` on the gateway device.

```python
python server.py
