from ultralytics import YOLO
import cv2
model = YOLO("yolov8_plant.pt")
results = model("./data/V001_tom1_00_061_e_14_20220101_27_06094434_40158887.png")
plots = results[0].plot()
cv2.imshow("plot", plots)
cv2.waitKey(0)
cv2.destroyAllWindows()
plots.save