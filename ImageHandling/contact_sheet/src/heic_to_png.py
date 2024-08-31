# convert heic to png.
# Assumptions:
# input folder contains only heic files
# Note that the png output is sent to the same folder,
# so that folder must be cleaned between runs
#----------------
# pip install pillow 
# pip install pillow_heif
import os
from PIL import Image
import pillow_heif

# Define the directory containing HEIC files
heic_directory = r"C:\temp\OneDrive-2024-08-31"

# Register HEIF plugin
pillow_heif.register_heif_opener()

# Loop through each file in the directory
for filename in os.listdir(heic_directory):
    input_file = os.path.join(heic_directory, filename)
    output_file = os.path.join(heic_directory, os.path.splitext(filename)[0] + ".png")
    
    # Convert the file to PNG
    with Image.open(input_file) as img:
        img.save(output_file, "PNG")

print("Conversion complete!")