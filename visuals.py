import os
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches

#Contains several methods for visualing the bounding boxes on the images
#Each method takes different forms of the bound box information

def draw_bounding_boxes_from_file(image_name, image_dir, label_dir):
    # classes = {
    #     "0": "undef", "1": "pedestrian", "2": "people", "3": "bicycle", "4": "car", 
    #     "5": "van", "6": "truck", "7": "tricycle", "8": "awning-tricycle", "9": "bus", 
    #     "10": "motor", "11": "other"
    # }

    image_path = os.path.join(image_dir, image_name)
    label_path = os.path.join(label_dir, image_name.replace('.jpg', '.txt'))
    
    image = Image.open(image_path)
    fig, ax = plt.subplots(1)
    ax.imshow(image)

    if os.path.exists(label_path):
        with open(label_path, 'r') as file:
            for line in file: #for each label
                parts = line.split()
                class_id = parts[0]
                cx, cy, bw, bh = map(float, parts[1:])

                x = (cx - bw / 2) * image.width #undo the noramlization
                y = (cy - bh / 2) * image.height
                width = bw * image.width
                height = bh * image.height

                #add the bounding box to the plot
                rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')
                ax.add_patch(rect)
                plt.text(x, y, class_id, color='white', fontsize=8, bbox=dict(facecolor='red', alpha=0.5))

    plt.axis('off')
    plt.show()

def draw_bounding_boxes_tensor(image_path, data_tensor):
    # classes = {
    #     "0": "undef", "1": "pedestrian", "2": "people", "3": "bicycle", "4": "car", 
    #     "5": "van", "6": "truck", "7": "tricycle", "8": "awning-tricycle", "9": "bus", 
    #     "10": "motor", "11": "other"
    # }

    
    image = Image.open(image_path)
    fig, ax = matplotlib.pyplot.subplots(1)
    ax.imshow(image)


    for box in data_tensor:
        class_id = box[5].item()
        x1 = round(box[0].item())
        y1 = round(box[1].item())
        x2 = round(box[2].item())
        y2 = round(box[3].item())

        rect = patches.Rectangle((x1, y1), x2-x1, y2-y1, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
        plt.text(x1, y1, class_id, color='white', fontsize=8, bbox=dict(facecolor='red', alpha=0.5))

    plt.axis('off')
    plt.show()

def draw_bounding_boxes_label(image_path, label_path):
    # classes = {
    #     "0": "undef", "1": "pedestrian", "2": "people", "3": "bicycle", "4": "car", 
    #     "5": "van", "6": "truck", "7": "tricycle", "8": "awning-tricycle", "9": "bus", 
    #     "10": "motor", "11": "other"
    # }
    
    image = Image.open(image_path)
    fig, ax = matplotlib.pyplot.subplots(1)
    ax.imshow(image)


    with open(label_path, 'r') as file:
            for line in file:
                parts = line.split()
                class_id = parts[0]
                cx, cy, bw, bh = map(float, parts[1:])

                x = (cx - bw / 2) * image.width
                y = (cy - bh / 2) * image.height
                width = bw * image.width
                height = bh * image.height

                rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')
                ax.add_patch(rect)
                plt.text(x, y, class_id, color='white', fontsize=8, bbox=dict(facecolor='red', alpha=0.5))

    plt.axis('off')
    plt.show()

image_directory = 'datasets/images/val'
label_directory = 'datasets/labels/val'
image_name = '0000001_02999_d_0000005.jpg'
draw_bounding_boxes_from_file(image_name, image_directory, label_directory)
