from flask import Flask, Response
import cv2

web_app = Flask(__name__)
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    raise RuntimeError("Webcam could not be started.")

def stream_video():
    while True:
        grabbed, image = video_capture.read()
        if not grabbed:
            break

        encoded, jpg_file = cv2.imencode(".jpg", image)
        if not encoded:
            continue

        image_data = jpg_file.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + image_data + b"\r\n"
        )

@web_app.route("/")
def index():
    return """
    <html>
        <head>
            <title>Real-Time Camera Stream</title>
        </head>
        <body>
            <h2>Webcam Video Feed</h2>
            <img src="/video_feed" width="640">
        </body>
    </html>
    """

@web_app.route("/video_feed")
def video_stream():
    return Response(
        stream_video(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
