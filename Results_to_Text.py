import os
import torch
from PIL import Image
import torchvision.transforms as transforms

def process_images(model, input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Define image transformation: assuming model requires input tensor normalized
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # Resize to the input size that the model expects
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # Iterate through each file in the input directory
    for filename in os.listdir(input_folder):
        if filename.endswith((".png", ".jpg", ".jpeg")):  # Check for image files
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            image = transform(image).unsqueeze(0)  # Add batch dimension
            
            # Model prediction
            outputs = model.predict(image_path)
            
            # Process each output (assuming there might be multiple outputs per image)
            for i, output in enumerate(outputs):
                boxes = output.boxes
                clas = boxes.cls
                dimensions = boxes.xywhn

                # Add class dimension and concatenate
                clas = clas.unsqueeze(1)
                boxes_combined = torch.cat((clas, dimensions), dim=1)

                # Saving the string to a text file
                output_file_path = os.path.join(output_folder, f"{filename}_output_{i}.txt")
                with open(output_file_path, 'w') as file:
                    for line in boxes_combined:
                        # Format each line as needed
                        formatted_line = ' '.join(f"{int(value):d}" if i == 0 else f"{value:.5f}" for i, value in enumerate(line.tolist()))
                        file.write(formatted_line + '\n')
