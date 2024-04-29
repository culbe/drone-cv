import os
import csv
import numpy as np
from PIL import Image

#method to convert the aannotions from the dataset into the format the model needs for training

def process_files(input_folder, output_folder, images_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):        
        if filename.endswith('.txt'):  
            image_file = filename.split('.')[0] +".jpg"
            image_file_path = os.path.join(images_folder, image_file)

            #Get image dimension
            try:
                img_dim = np.asarray(Image.open(image_file_path)).shape
            except:
                #no matching image
                print("missing image " + image_file_path)
                continue
            image_width = img_dim[1]
            image_height = img_dim[0]

            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)

            with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
                
                reader = csv.reader(input_file)

                for row in reader:
                    x = int(row[0])
                    y = int(row[1])
                    category = row[5]
                    width = int(row[2])
                    height = int(row[3])
                    #make normalized and centered values
                    new_x = str(round((x+width/2)/image_width, 5))
                    new_y = str(round((y+height/2)/image_height, 5))
                    new_width = str(round(width/image_width, 5))
                    new_height = str(round(height/image_height, 5))
                    reordered_row = category + ' ' + new_x + ' ' + new_y + ' ' + new_width + ' ' + new_height
                    output_file.write(reordered_row + '\n')

#Run the process
input_folder = 'datasets/raw_annotations/train'
output_folder = 'datasets/labels/train'
image_folder = 'datasets/images/train'
process_files(input_folder, output_folder, image_folder)