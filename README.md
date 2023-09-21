# YOLOv8 Annotation Converter

This Python script is designed to convert annotations from the VIA image annotation tool into YOLOv8 format annotations. YOLOv8 is a popular object detection framework that requires a specific annotation format.

The script reads annotation data from a JSON file exported by the VIA tool, processes the data, and generates YOLOv8 instance segmentation style annotation files along with organizing the corresponding images.

## Requirements

- Python 3.x
- Pillow (PIL) library
- JSON data exported from the VIA annotation tool

## How to Use

1. Clone or download this repository to your local machine.

2. Install the required dependencies using the following command:

   pip install pillow
   
Prepare your annotation data and images:

Export annotation data from the VIA tool in JSON format.
Place your annotation JSON file in the same directory as the script.
Organize your images in a folder and specify its path in the image_source variable in the script.
Run the script using the following command:

python convert_annotations.py
This will generate YOLOv8 style annotation files and organize the images in the output folders.

Check the train/labels and train/images folders for the converted annotations and corresponding images.

Additionally, you have a new script called vgg2pngSeg, which can be used for a different purpose. Make sure to check its functionality and instructions in the script file.

Configuration
json_file_path: Path to the JSON file containing annotation data.
output_folder: The folder where annotation files and images will be organized.
image_source: Path to the folder containing your images.
Contributing
Contributions are welcome! If you find any issues or want to enhance the script, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.