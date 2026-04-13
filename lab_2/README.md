# Lab 2 - Multi-Sensor IoT Dashboard

## Student Submission

This lab demonstrates a multi-sensor IoT monitoring system using socket communication, MQTT, and Grafana. The system is designed to simulate multiple sensor readings, transfer them through an edge device, and display them on a real-time dashboard.

---

## 1. System Overview

The system is made up of four components:

### Sensor Node (Laptop 1)
Laptop 1 works as the sensor node. It uses socket communication to simulate and send three different sensor values:
- temperature
- humidity
- light

### Edge Device (Laptop 2)
Laptop 2 acts as the edge device. It receives the sensor data from the sensor node and forwards the values to an MQTT broker.

### MQTT Broker
The MQTT broker functions as the central communication point of the system. It receives the published messages and makes them available to subscribers.

### Grafana Dashboard (Laptop 1)
Grafana runs on Laptop 1 and displays the sensor values in real time on a dashboard with four panels.

---

## 2. Sensor Nodes

The system simulates the following sensor data:

- **Temperature Sensor:** random temperature values between **20 and 35°C**
- **Humidity Sensor:** random humidity values between **40 and 80%**
- **Light Sensor:** random light intensity values between **100 and 1000 lux**

---

## 3. MQTT Topics Used

The following MQTT topics are used in this system:

- `savonia/iot/temperature` for temperature readings
- `savonia/iot/humidity` for humidity readings
- `savonia/iot/light` for light intensity readings

---

## 4. Grafana Dashboard Layout

The Grafana dashboard contains four panels:

1. **Temperature Graph**  
   A graph that shows how the temperature changes over time.

2. **Humidity Gauge**  
   A gauge that displays the current humidity percentage.

3. **Light Gauge**  
   A gauge that displays the current light intensity in lux.

4. **Status Panel**  
   A panel that shows the status of the sensors, including temperature, humidity, and light.

---

## 5. Screenshot of the 4-Panel Dashboard

After running Grafana and connecting it to the MQTT topics, add the dashboard screenshot here before submission.

**[Insert your 4-panel Grafana dashboard screenshot here]**

---

## 6. Explanation of Dashboard Layout

The dashboard is created for real-time monitoring of the three simulated sensor values: temperature, humidity, and light. The temperature graph helps show changes over time, while the humidity and light gauges display the most recent values clearly. The status panel provides a quick overview of the sensor conditions.

---

## 7. Reflection Question

### Why do we separate each sensor into a different MQTT topic?

Each sensor is placed in a separate MQTT topic so that the data streams can be tracked, monitored, and processed independently. This makes the system easier to manage and also provides more flexibility when scaling the solution or handling each type of sensor data separately.

---

## 8. Conclusion

This lab shows how a multi-sensor IoT system can be built by combining socket communication, MQTT, and Grafana. The sensor node generates multiple values, the edge device forwards them to the broker, and Grafana visualizes the data in real time. The system demonstrates a simple but effective method for monitoring multiple sensor streams in one dashboard.
