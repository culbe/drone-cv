import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

classes = {"0":"undef", "1":"pedestrian", "2":"people", "3":"bicycle", "4":"car", "5":"van", "6":"truck", \
           "7":"tricycle", "8":"awning-tricycle", "9":"bus", "10":"motor", "11":"other"}

def make_image(annotations, image_path, save_path):
    img = np.asarray(Image.open(image_path))

    print(img.shape)
    im_width = img.shape[1]
    im_height = img.shape[0]

    fig, ax = plt.subplots()

    ax.imshow(img)


    anno_arr = annotations.split('\n')

    for line in anno_arr:
        data = line.split(' ')
        if(len(data)!=5):
            continue
        width = round(float(data[3])*im_width)
        height = round(float(data[4])*im_height)
        
    rect = patches.Rectangle((0, 100), 30, 40, linewidth=1, edgecolor='r', facecolor='none')

    ax.add_patch(rect)

    
    plt.text(0,100,"class", color='w')
    plt.savefig(save_path)
    plt.show()


make_image("something", "datasets/images/val/0000360_06861_d_0000748.jpg", "testvis.png")
    
# print(round(float("0.3523")))