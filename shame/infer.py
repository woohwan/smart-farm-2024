from ultralytics import YOLO

# model = YOLO("yolov8.plant.torchscript", task='detect')
model = YOLO("model_classfication_plant.pt", task='detect')
results = model(["data/3.png"], imgsz=640)

print(results[0].tojson())

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    print(boxes)
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    # result.show()  # display to screen
    # result.save(filename='result.jpg')  # save to disk
