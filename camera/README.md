# Automated Video Capture and Transfer System

## Overview

This project demonstrates an automated video handling system that records short video clips, stores them temporarily on the sender device, and transfers them to another device through the network. After the receiver successfully confirms that the file has been received, the sender removes its local copy.

---

## Components

### Sender
The sender device is responsible for capturing video clips and sending them to the receiver over the network.

### Receiver
The receiver device accepts the incoming video files and saves them for storage.

---

## Files

- `sender.py` – Runs on the sender device and handles video capture and file transfer
- `receiver.py` – Runs on the receiver device and manages receiving and saving video files
- `videos/` – Folder where the sender stores video clips before they are transferred
- `received_videos/` – Folder where the receiver stores the transferred video files

---

## How to Run

### Receiver

Run the following command on **Laptop B**:

```python
python receiver.py
