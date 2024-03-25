from ultralytics import YOLO
model = YOLO("yolov8_plant.pt")
results = model.predict("data/V001_tom1_00_061_e_14_20220101_27_06094434_40158887.png")
print(results[0].save('0.jpeg'))
