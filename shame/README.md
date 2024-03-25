```  
# only CPU mode
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt



# archive
torch-model-archiver --model-name yolov8 --version 1.0 --serialized-file yolov8_plant.pt --handler custom_handler.py

# start
torchserve --start --model-store model_store --ncs 
# or
torchserve --start --model-store model_store  --models yolov8=yolov8.mar

# register model
curl -X POST "localhost:8081/models?model_name=yolov8&url=yolov8.mar&initial_workers=4&batch_size=2"
```  