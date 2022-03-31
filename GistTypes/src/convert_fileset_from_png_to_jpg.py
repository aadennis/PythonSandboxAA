from PIL import Image
import io
import glob
import os

"""
Convert a batch of png files to jpg, so that the tags field is accessible in the exif metadata.
The source file is not changed or deleted.
RN, the function only supports source files with the format "*iOS.png" as my interest is in 
IOS photos
"""
def convert_fileset_from_png_to_jpg(folder):

    PNG_WILDCARD = "*iOS.png"
    JPG = ".JPG"

    if not os.path.exists(folder):
        raise FileNotFoundError(f"No folder [{folder}]. Exiting...")
    
    print(folder)
    joint = folder + "/" + PNG_WILDCARD

    f = glob.glob(joint)
    count = len(f)
    print(f"there are [{count}] items in folder [{folder}] with wildcard [{PNG_WILDCARD}]")

    ctr = 0
    for src_filename in f:
        if ctr%20 == 0:
            print(f"Processing file [{ctr}] of [{count}]")
        ctr += 1

        src_base = os.path.basename(src_filename)
        file_root = os.path.splitext(src_base)[0]

        target_name = dir + "/" + file_root + JPG

        im = Image.open(src_filename)
        rgb_im = im.convert('RGB')
        rgb_im.save(target_name)
    print("Done.")

if __name__ == "__main__":
    dir = "D:\onedrive\data\photos\_Albums\CameraRollDump\CRD_2021_11"
    convert_fileset_from_png_to_jpg(dir)