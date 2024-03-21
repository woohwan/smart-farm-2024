참고  
- https://medium.com/@pumaline/use-torchserve-with-a-customized-handler-script-f7d329e78ba4  
- https://github.com/pytorch/serve/tree/master/examples/image_classifier/mnist  
```  
chmod +rwx model.py
cd serve/examples/image_classifier/
chmod +rwx index_to_name.json
```  

```  
torch-model-archiver --model-name mnist --version 1.0 --model-file mnist.py --serialized-file mnist_cnn.pt --handler  mnist_handler.py  
```  