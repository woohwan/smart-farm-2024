from ultralytics import YOLO
model = YOLO("yolov8_plant.pt")
results = model.predict("data/V001_tom1_00_085_e_15_20220101_27_05110138_38102607.png")
print(results)
