# Socket Programming with Python

## Project Description

This project demonstrates a simple TCP client-server communication program written in Python. The server waits for a client to connect and receives temperature-like sensor data. The client connects to the server and sends random temperature values every 5 seconds.

The purpose of this project is to show how socket programming can be used in Python for communication between two devices over a network.

## Files

- `server.py` → Receives data from the client and displays the incoming messages
- `client.py` → Creates random temperature values and sends them to the server
- `README.md` → Contains the project explanation and summary

## Requirements

- Python 3.x

## How to Run

### 1. Run the server

```python
python server.py
