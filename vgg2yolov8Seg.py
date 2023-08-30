from PIL import Image
import json
import os
import shutil

def convert_to_yolov8_annotation(region, image_width, image_height):
    x_values = region["shape_attributes"]["all_points_x"]
    y_values = region["shape_attributes"]["all_points_y"]

    # Normalize the coordinates of the points
    x_values = [x / image_width for x in x_values]
    y_values = [y / image_height for y in y_values]

    # Combine the coordinates into a single string
    coordinates = []
    for x, y in zip(x_values, y_values):
        coordinates.append(f"{x:.6f} {y:.6f}")
    coordinates = " ".join(coordinates)

    # Add the object class index at the beginning of the string
    class_index = 0
    return f"{class_index} {coordinates}"

# Path to the .json file containing the data
json_file_path = "./via_region_data_train.json"
output_folder = "train"  # Folder where annotation and image files will be saved
image_source = "./images"  # Path to all annotation images

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

labels_output_folder = os.path.join(output_folder, "labels")  # Folder where labels will be saved
images_output_folder = os.path.join(output_folder, "images")  # Folder where images will be saved

if not os.path.exists(labels_output_folder):
    os.makedirs(labels_output_folder)
if not os.path.exists(images_output_folder):
    os.makedirs(images_output_folder)

with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

for image_id, image_data in json_data.items():
    filename = image_data["filename"]
    regions = image_data["regions"]

    # Copy the image to the images output folder
    image_source_path = os.path.join(image_source, filename)
    image_destination_path = os.path.join(images_output_folder, filename)
    shutil.copyfile(image_source_path, image_destination_path)

    # Load the image to get its dimensions
    image = Image.open(image_destination_path)
    image_width, image_height = image.size

    annotations = []
    for region in regions:
        yolov8_annotation = convert_to_yolov8_annotation(region, image_width, image_height)
        annotations.append(yolov8_annotation)

    # Write the annotations to a .txt file in the 'labels' folder
    label_filename = os.path.join(labels_output_folder, f"{os.path.splitext(filename)[0]}.txt")
    with open(label_filename, "w") as label_file:
        label_file.write("\n".join(annotations))

print("Annotations and images successfully created in the 'val/labels' and 'val/images' structure.")
