# Lab 3 - Real-Time Monitoring with YOLO Detection

## Participants

- **Sender (Laptop A):** [Your Name]
- **Viewer (Laptop B):** [Partner Name]

## Sender IP Address

`192.168.x.x`

## System Working

In this system, the sender device (Laptop A) launches a Flask server that streams live video captured from the webcam.

The viewer device (Laptop B) receives the video stream, applies YOLO detection to each frame, and displays the detection results in real time.

## Instructions to Run the System

### On Laptop A

Run the `app.py` file to start the webcam video stream.

```python
python app.py
