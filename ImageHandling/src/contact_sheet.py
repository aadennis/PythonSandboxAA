# Credit for original: https://code.activestate.com/recipes/ (join lines)
# 578267-use-pil-to-make-a-contact-sheet-montage-of-images/
import os
import glob
import math
from PIL import Image
from pillow_heif import register_heif_opener

def make_contact_sheet(img_folder, img_type):
    """\
    Make a contact sheet using all the files of the given
    file type in the given folder. Right now, the number of columns is
    a constant. The number of rows is ceil(file_count / number of columns).
    That means for instance, if you have 5 images in a folder, and the 
    number of columns (constant) is 3, then you get 2 rows: the first row
    has 3 images, and the second row has 2, with a blank at the right hand side.

    Parameters:
    img_folder   path to the folder with the source image files
    img_type     Image type. For example, jpg, png, tiff.
                 The script dumbly uses the img_type, so make sure
                 it is a valid type. The script handles mixed-case OK.

    Right now, you have no control over size, margins etc.
    Returns a PIL image object.
    """

    # Set size, margins, padding
    maxcols = 3
    photow = 100
    photoh = 100
    marl = mart = marr = marb = padding = 5
    marw = marl + marr
    marh = mart + marb

    file_path = img_folder + "/*" + img_type

    # count the images, so we know how to arrange the rows 
    # and columns
    files = os.listdir(img_folder)
    file_count = 0
    for file in files:
        if file.lower().endswith(img_type):
            file_count += 1

    nrows = math.ceil(file_count/maxcols)
    padw = (maxcols - 1) * padding
    padh = (nrows - 1) * padding
    isize = (maxcols * photow + marw + padw, nrows * photoh + marh + padh)
    white = (255, 255, 255)
    contact_sheet = Image.new('RGB', isize, white)

    # Iterate over the (initially) empty contact sheet image.
    icol = 0
    irow = 0
    for img_in_path in glob.iglob(file_path):
        img = Image.open(img_in_path).resize((photow, photoh))
        left = marl + icol * (photow + padding)
        right = left + photow
        upper = mart + irow * (photoh + padding)
        lower = upper + photoh
        bbox = (left, upper, right, lower)
        contact_sheet.paste(img, bbox)
        icol += 1
        if (icol >= maxcols):
            icol = 0
            irow += 1

    # Done - return the contact sheet
    return contact_sheet

#--------------------------------------------
# arrange
img_folder = "tests/TestImageFiles"
img_type = ".jpg"
contact_sheet = make_contact_sheet(img_folder,img_type)
contact_sheet_file = "c:/temp/outish.jpg"
# act
contact_sheet.save(contact_sheet_file)