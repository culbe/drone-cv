def draw_bounding_boxes(image_dir, label_dir, classes):
    # List all image files in the directory
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]

    # Initialize counter
    counter = 0

    for image_file in image_files:
        if counter < 10:  # Check if counter is less than 10
            # Construct the full path to the image and label file
            image_path = os.path.join(image_dir, image_file)
            label_path = os.path.join(label_dir, image_file.replace('.jpg', '.txt').replace('.png', '.txt'))
            
            # Load the image
            image = Image.open(image_path)
            fig, ax = plt.subplots(1)
            ax.imshow(image)

            # Check if label file exists
            if os.path.exists(label_path):
                with open(label_path, 'r') as file:
                    for line in file:
                        parts = line.split()
                        class_id = parts[0]  # Keep class id as number
                        cx, cy, bw, bh = map(float, parts[1:])  # Convert string to float

                        # Convert from normalized to image coordinates
                        x = (cx - bw / 2) * image.width
                        y = (cy - bh / 2) * image.height
                        width = bw * image.width
                        height = bh * image.height

                        # Create a Rectangle patch
                        rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')
                        ax.add_patch(rect)
                        # Add class label text with class number
                        plt.text(x, y, class_id, color='white', fontsize=8, bbox=dict(facecolor='red', alpha=0.5))

            # Display the image with bounding boxes
            plt.axis('off')
            plt.show()

            # Increment counter
            counter += 1
        else:
            break  # Break the loop after processing 10 images
            
classes = {
    "0": "undef", "1": "pedestrian", "2": "people", "3": "bicycle", "4": "car", 
    "5": "van", "6": "truck", "7": "tricycle", "8": "awning-tricycle", "9": "bus", 
    "10": "motor", "11": "other"
}

# Usage example
image_directory = 'datasets/images/val'
label_directory = 'datasets/labels/val'
draw_bounding_boxes(image_directory, label_directory, classes)