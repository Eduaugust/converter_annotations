from PIL import Image, ImageDraw
import json
import os
import shutil

def create_binary_mask(regions, image_width, image_height):
    # Create a blank image with a white background
    mask = Image.new("1", (image_width, image_height), 0)

    draw = ImageDraw.Draw(mask)

    for region in regions:
        x_values = region["shape_attributes"]["all_points_x"]
        y_values = region["shape_attributes"]["all_points_y"]

        # Normalize the coordinates of the points
        x_values = [x / image_width for x in x_values]
        y_values = [y / image_height for y in y_values]

        # Create a list of tuples for polygon points
        polygon_points = [(x * image_width, y * image_height) for x, y in zip(x_values, y_values)]

        # Draw the filled polygon
        draw.polygon(polygon_points, outline=1, fill=1)

    return mask

# Path to the .json file containing the data
json_file_path = "./via_region_data_test.json"
output_folder = "test"  # Folder where annotation and image files will be saved
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

    mask = create_binary_mask(regions, image_width, image_height)

    # Save the mask as a PNG file
    mask_filename = os.path.join(labels_output_folder, f"{os.path.splitext(filename)[0]}.png")
    mask.save(mask_filename)

print("Annotations and images successfully created in the 'val/labels' and 'val/images' structure.")
