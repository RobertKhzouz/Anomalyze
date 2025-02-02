import os
from fullmodel.fullmodel import *
from flask import Flask, jsonify, Response
import random
from flask_cors import CORS
from interactive_sql import Commands
from mqtt_sub import init_mqtt
import threading
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Enable CORS for all routes
socketio = SocketIO(app, cors_allowed_origins="*")

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:5173"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

@app.route("/api/fetch_all", methods=["GET"])
def api_fetch_all():
    return Commands.fetch_all()

@app.route("/api/fetch_latest", methods=["GET"])
def api_fetch_latest(n=1):
    return Commands.fetch_latest(n)

@app.route("/api/insert_row", methods=["GET"])
def api_insert_row(sensor_id: str, temperature: float, pressure: float):
    return Commands.insert_sensor(sensor_id, temperature, pressure)

@app.route("/api/insert_bulk", methods=["GET"])
def api_insert_bulk(sensor_readings: list):
    return Commands.insert_bulk_sensors(sensor_readings)

@app.route("/api/delete_sensor", methods=["GET"])
def api_delete_sensor(sensor_id):
    return Commands.delete_sensor(sensor_id)

@app.route("/api/delete_all", methods=["GET"])
def api_delete_all():
    return Commands.delete_all()


mqtt_thread = threading.Thread(target=init_mqtt, daemon=True)
mqtt_thread.start()

# def send_images():
#     while True:
#         image_url = f"/images/image_{random.randint(1, 5)}.jpg"
#         socketio.emit("update_image", image_url)

IMAGE_PATH = "static/current_image.jpg"
# def image_handler():
#     last_modified = None
#     while True:
#         if os.path.exists(IMAGE_PATH):
#             modified_time = os.path.getmtime(IMAGE_PATH)
#             if modified_time != last_modified:
#                 last_modified = modified_time
#                 socketio.emit("update_image", IMAGE_PATH)
#
# def handle_connect():
#     socketio.start_background_task(send_images)


@app.route('/video_feed')
def video_feed():
    """Route to stream processed video frames."""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, port=5050)
    socketio.run(app, host="0.0.0.0", port=5000)