#!/bin/sh
torch-model-archiver --model-name mnist --version 2.0 --model-file mnist.py --serialized-file mnist_cnn.pt --handler mnist_handler.py