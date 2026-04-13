import cv2
from ultralytics import YOLO

VIDEO_SOURCE = "http://192.168.1.20:5000/video_feed"  # Change this to Laptop A IP

# Load the YOLO model
detector = YOLO("yolov8n.pt")  # Change this if your model file is different

# Open the video stream from Laptop A
video_stream = cv2.VideoCapture(VIDEO_SOURCE)

if not video_stream.isOpened():
    print("Error: Unable to connect to the video stream.")
    raise SystemExit

print("Video stream connected. Starting YOLO object detection...")

while True:
    success, image = video_stream.read()
    if not success:
        print("Error: Failed to receive a frame from the stream.")
        break

    # Perform detection on the current frame
    detection_results = detector(image)

    # Draw detection boxes and labels on the frame
    output_frame = detection_results[0].plot()

    # Show the processed frame
    cv2.imshow("Real-Time YOLO Detection", output_frame)

    # Press q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_stream.release()
cv2.destroyAllWindows()
