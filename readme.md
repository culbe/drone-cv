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

The command used to run the training the MAGIC envirmonment was:

```
yolo detect train data=dataset_configuration.yaml model=yolov8n.pt epochs=500
```

We used jupyter notebook as a sort of stratch paper - visually evaulating the performance of the model and running some of the methods contained in the other files. This file was not included because it was only temporary work.

Much more information on our processes can be found in the final report.
