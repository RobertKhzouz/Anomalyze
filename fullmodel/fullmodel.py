from ultralytics import YOLO


# Load models once (so they are not reloaded on every request)
animal_model = YOLO('fullmodel/yolov8n.pt')  # Animal detection model
knife_model = YOLO('fullmodel/weights.pt')    # Knife detection model

# Define class filters for each model
ANIMAL_CLASSES = {"dog", "cat", "bird", "horse", "cow", "sheep", "elephant", "bear", "zebra", "giraffe"}
KNIFE_CLASSES = {"knife"}

# Export models and class filters for use in Flask
__all__ = ["animal_model", "knife_model", "ANIMAL_CLASSES", "KNIFE_CLASSES"]
