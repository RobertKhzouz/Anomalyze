from flask import Flask, Response
import cv2
from fullmodel.fullmodel import animal_model, knife_model, ANIMAL_CLASSES, KNIFE_CLASSES



def detect_objects(image, model, class_filter, color):
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

def detect_animals_and_knives(image):

    if image is None:
        return "Error: Could not load image", 400

    # Run both models on the same image
    detect_objects(image, animal_model, ANIMAL_CLASSES, (0, 255, 0))  # Green for animals
    detect_objects(image, knife_model, KNIFE_CLASSES, (0, 0, 255))  # Red for knives

    # Convert processed image to bytes
    _, buffer = cv2.imencode('.jpg', image)
    image_bytes = buffer.tobytes()

    # Return the image as an HTTP response
    return Response(image_bytes, mimetype='image/jpeg')

