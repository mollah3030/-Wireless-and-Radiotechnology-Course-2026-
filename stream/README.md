# Real-Time Video Streaming System

## Overview

This project presents a simple real-time home monitoring system built with Flask and OpenCV. The system captures live video from a webcam on the sender device (Laptop A) and streams it through the local network to the viewer device (Laptop B).

---

## Files Included

- `app.py` – The sender-side program that captures webcam video and streams it over the local network
- `receiver.py` – The viewer-side program for Laptop B, which would be used to receive and display the video stream in a browser  
  *(This file is not included here.)*

---

## Instructions

### Step 1: Run the Sender Program

On **Laptop A**, start the video stream by running:

```python
python app.py
