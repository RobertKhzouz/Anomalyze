import cv2
from ultralytics import YOLO

# Open webcam
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Load YOLO models
animal_model = YOLO('yolov8n.pt')  # Animal detection model
knife_model = YOLO('weights.pt')   # Knife detection model

# Define class filters
ANIMAL_CLASSES = {"dog", "cat", "bird", "horse", "cow", "sheep", "elephant", "bear", "zebra", "giraffe"}
KNIFE_CLASSES = {"knife"}

def detect_objects(image, model, class_filter, color):
    """Detect objects using YOLO model and draw bounding boxes."""
    results = model(image)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            confidence = box.conf[0].item()
            class_id = int(box.cls[0].item())

            class_name = model.names[class_id]

            if class_name in class_filter:
                cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
                label = f"{class_name}: {confidence:.2f}"
                cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

def generate_frames():
    """Capture frames, process them, and stream as MJPEG video."""
    while True:
        success, frame = cap.read()
        if not success:
            break

        # Run object detection on the frame
        detect_objects(frame, animal_model, ANIMAL_CLASSES, (0, 255, 0))  # Green for animals
        detect_objects(frame, knife_model, KNIFE_CLASSES, (0, 0, 255))    # Red for knives

        # Encode frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # Yield the frame in the MJPEG format
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
