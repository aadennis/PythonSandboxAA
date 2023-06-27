# Credit: https://code.activestate.com/recipes/
# 578267-use-pil-to-make-a-contact-sheet-montage-of-images/
import os
import glob
from PIL import Image
from pillow_heif import register_heif_opener

def make_contact_sheet(img_folder, img_type):
    """\
    Make a contact sheet using all the files of the given
    file type in the given folder.

    img_folder   path to the folder with the source image files
    img_type     image type. For example, jpg, png, tiff.
                 The script dumbly uses the img_type, so make sure
                 it is a valid type.

    Right now, you have no control over size margins etc.
    Returns a PIL image object.
    """

    # Set size, margins, padding
    maxcols = 5
    nrows = 1
    photow = 100
    photoh = 100
    marl = mart = marr = marb = padding = 5
    marw = marl + marr
    marh = mart + marb
    padw = (maxcols - 1) * padding
    padh = (nrows - 1) * padding
    isize = (maxcols * photow + marw + padw, nrows * photoh + marh + padh)

    file_path = img_folder + "/*" + img_type

    white = (255, 255, 255)
    inew = Image.new('RGB', isize, white)

    icol = 0
    irow = 0
    for img_in_path in glob.iglob(file_path):
        img = Image.open(img_in_path).resize((photow, photoh))
        left = marl + icol * (photow + padding)
        right = left + photow
        upper = mart + irow * (photoh + padding)
        lower = upper + photoh
        bbox = (left, upper, right, lower)
        inew.paste(img, bbox)
        icol += 1
        if (icol >= maxcols):
            icol = 0
            irow += 1
    return inew

#--------------------------------------------
# arrange
img_folder = "tests/TestImageFiles"
img_type = ".jpg"
contact_sheet = make_contact_sheet(img_folder,img_type)
contact_sheet_file = "c:/temp/outish.jpg"
# act
contact_sheet.save(contact_sheet_file)