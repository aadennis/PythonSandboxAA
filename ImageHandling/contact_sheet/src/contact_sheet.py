# Credit for original: https://code.activestate.com/recipes/ (join lines)
# 578267-use-pil-to-make-a-contact-sheet-montage-of-images/
import os
import glob
import math
from PIL import Image
from pillow_heif import register_heif_opener

def is_image_file(full_path_name):
    for file_type in ("jpg", "jpeg","png","heic"):
        if full_path_name.lower().endswith(file_type):
            return True
    return False

def make_contact_sheet(img_folder,  output_file, max_images = 100, column_count = 3):
    """\
    Make a contact sheet using all the files of the given
    file type in the given folder. The number of rows displayed is
    a function of the number of display columns requested by the user - 
     see the function signature for the current default. 
    Basically the number of display rows is ceil(file_count / 
    number of columns).
    That means for instance, if you have 5 images in a folder, and the 
    number of columns (constant) is 3, then you get 2 rows: the first row
    has 3 images, and the second row has 2, with a blank at the right hand side.

    Parameters:
    img_folder   path to the folder with the source image files
    img_type     Image type. For example, jpg, png, tiff.
                 The script dumbly uses the img_type, so make sure
                 it is a valid type. The script handles mixed-case OK.
    column_count The number of columns to be displayed. Default is 3.

    Right now, you have no control over size, margins etc.
    Returns a PIL image object.
    """

  

    #required for HEIC support
    register_heif_opener()

    # Set size, margins, padding
    photow = photoh = 100
    marl = mart = marr = marb = padding = 5
    marw = marl + marr
    marh = mart + marb

    # count the images, so we know how to arrange the rows 
    # and columns
    file_list = []
    files = os.listdir(img_folder)
    file_count = 0
    for file in files:
        if is_image_file(file):
            file_count += 1
            file_list.append(file)
            if file_count > max_images:
                break
  
    

    nrows = math.ceil(file_count/column_count)
    print(f"Processing [{file_count}] images")
    print(f"max_images: {max_images}")
    print(f"column_count: {column_count}")
    print(f"estimated row_count: {nrows}")

    padw = (column_count - 1) * padding
    padh = (nrows - 1) * padding
    isize = (column_count * photow + marw + padw, nrows * photoh + marh + padh)
    white = (255, 255, 255)
    contact_sheet = Image.new('RGB', isize, white)

    # Iterate over the (initially) empty contact sheet image.
    icol = 0
    irow = 0

    for file in file_list:
       
        img_in_path = img_folder + "/" + file
        img = Image.open(img_in_path).resize((photow, photoh))
        left = marl + icol * (photow + padding)
        right = left + photow
        upper = mart + irow * (photoh + padding)
        lower = upper + photoh
        bbox = (left, upper, right, lower)
        contact_sheet.paste(img, bbox)
        icol += 1
        if (icol >= column_count):
            icol = 0
            irow += 1
            if irow%10 == 0:
                print(f"Processing row {irow}")

    print(f"Contact sheet is saved as [{output_file}]")
    contact_sheet.save(output_file)
    # Done - return the contact sheet
    return contact_sheet

