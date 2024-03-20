```   
# archive
torch-model-archiver --model-name yolov8 --version 1.0 --handler custom_handler.py  

# start server
torchserve --start --model-store model_store --ncs

# create worker  
curl -X POST "localhost:8081/models?model_name=yolov8&url=yolov8.mar&initial_workers=4&batch_size=2"
