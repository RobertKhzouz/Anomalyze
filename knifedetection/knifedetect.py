import cv2
from ultralytics import YOLO


weights = 'knifedetection/weights.pt'
model = YOLO(weights)

image = cv2.imread('knifedetection/test.png')

def KnifeDetect(image, model = YOLO(weights)):
    if image is None:
        print("Error: Could not load image")
        exit()
    results = model(image)
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            confidence = box.conf[0].item()
            class_id = int(box.cls[0].item())

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

            class_name = model.names[class_id]

            label = f"Class {class_id}: {confidence:.2f}"
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)
    cv2.imshow('Detections', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if class_id:
        return True
    else:
        return False