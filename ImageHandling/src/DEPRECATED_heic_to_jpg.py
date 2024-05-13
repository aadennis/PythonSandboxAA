# Convert a folder containing HEIC image files
# from heic to jpg. The original files remain.
# The new files are stored in the same folder.
# Only tested on Windows, where desktop.ini makes a
# fleeting appearance. Hence the check for .HEIC extension.
#
# prerequisites:
# pip install Pillow
# pip install Pillow_heif

import os
from PIL import Image
from pillow_heif import register_heif_opener

def convert_heic_to_jpg(path):
    files = os.listdir(path)
    heic_found = False
    register_heif_opener()

    for file in files:
        filename = os.path.splitext(file)
        file_prefix = filename[0]
        file_extension = filename[1]
        if file_extension.upper() == ".HEIC":
            heic_found = True
            print(f"Converting: {file}")
            im = Image.open(path+file)
            rgb_im = im.convert("RGB")
            rgb_im.save(path+file_prefix+'_from_heic'+'.jpg')

    if not heic_found:
        print(f"No heic files found in folder [{path}]")

# Call the function with the path to the folder containing the HEIC files
convert_heic_to_jpg("c:/temp/")
