import os
import csv
import numpy as np
from PIL import Image


#Method to size all images to 640x640
#I think the model was already doing this automatically, but doing it beforehand saves training time
def process_files(input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):        
        if filename.endswith('.jpg'):  
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)

            output_image = Image.open(input_file_path).resize((640,640))

            output_image.save(output_file_path)

input_folder = 'datasets/images/val'
output_folder = 'datasets/images_640/val'
process_files(input_folder, output_folder)