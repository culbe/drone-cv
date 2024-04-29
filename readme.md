# Drone object detection

The dataset directory has been excluded because of its extremely large size, but can be seen in the github: https://github.com/culbe/drone-cv  It is formated as such:

dataset

    -images

    -train

    -val

    -images_640

    -train

    -val

-labels (txt files)

    -train

    -val

-raw_annonations (txt files)

    -train

    -val

For the actual training runs on the MAGIC gpu's, the resized 640 images were placed in the images folder and the original images were not uploaded (nor were the raw annotations).

The command used to run the training the MAGIC environment was:

```
yolo detect train data=dataset_configuration.yaml model=yolov8n.pt epochs=500
```

The yolov8n.pt file specifies the pretrained weights and also implictly the model architecture. It is automatically downloaded on the first run.

The yaml file is our own config file specifying the training and validation dataset.


The trainingResults folder was also too large to submit because of the weights files. It contains lots of performance metrics and, most importantly the weights files that encapture all the training done. It can also be seen in the github. 


We used jupyter notebook as a sort of stratch paper - visually evaulating the performance of the model and running some of the methods contained in the other files. We did not include this temporary stratch work, but an examples.ipynb file is included as a reference for how to run and manual evaluate the model.

Much more information on our processes can be found in the final report.
