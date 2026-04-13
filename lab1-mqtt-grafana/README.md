# Lab 1 - Real-Time MQTT Monitoring with Grafana

## Student Submission

This lab continues the earlier IoT pipeline by adding a real-time monitoring dashboard with Grafana.

## 1. Short Description of the Full System

This setup uses two laptops.

- **Laptop 1** acts as the sensor device and sends temperature readings through socket programming.
- **Laptop 2** acts as the edge device. It receives the socket data and then publishes it to an MQTT broker.
- **Grafana** runs on Laptop 1, connects to the same MQTT topic, and shows the received values live.

So, the full data path is:

**Laptop 1 (Sensor) → Socket → Laptop 2 (Edge Device) → MQTT Broker → Grafana on Laptop 1**

## 2. Socket Data Flow from Laptop 1 to Laptop 2

The file **`socket_sensor.py`** runs on **Laptop 1**.

Its role is to:

- create a TCP socket client
- connect to Laptop 2 using port 5000
- generate simulated temperature readings
- send one value every 2 seconds

The file **`edge_device.py`** runs on **Laptop 2**.

Its role is to:

- create a TCP socket server on port 5000
- receive incoming sensor data from Laptop 1
- read each temperature reading
- publish the same reading to the MQTT topic

## 3. MQTT Topic Used

`savonia/iot/temperature/adnan`

## 4. Broker Used

`broker.emqx.io`

**Port used:**

`1883`

## 5. Files in This Repository

- `socket_sensor.py`
- `edge_device.py`
- `README.md`

## 6. How to Run the System

### Laptop 2 (Edge Device)

First, install the MQTT library:

```python
pip install paho-mqtt
