import os
import csv

def process_files(input_folder, output_folder):
    image_width = 1920
    image_height = 1080

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):  
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)

            with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
                
                reader = csv.reader(input_file)
                writer = csv.writer(output_file)

                for row in reader:
                    x = int(row[0])
                    y = int(row[1])
                    category = row[5]
                    width = int(row[2])
                    height = int(row[3])
                    reordered_row = [category, (x+width/2)/image_width, (y+height/2)/image_height, width/image_width, height/image_height]
                    writer.writerow(reordered_row)

input_folder = 'raw_annotations/val'
output_folder = 'labels/val'
process_files(input_folder, output_folder)