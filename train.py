from ultralytics import YOLO

model = YOLO("yolov8n-pose.pt")

model.train(
    data="dataset/data.yaml",
    epochs=100,
    imgsz=1280,
    batch=8,
    device='mps',
    patience=20,
    project="court_model",
    name="run1"
)