# Credit for original: https://code.activestate.com/recipes/ (join lines)
# 578267-use-pil-to-make-a-contact-sheet-montage-of-images/
import os
import glob
import random
import math
from PIL import Image
from pillow_heif import register_heif_opener

class ContactSheet:


    def __init__(self, img_folder,  max_images=100, column_count=3):
        self.img_folder = img_folder
        self.max_images = max_images
        self.column_count = column_count
        self.make_contact_sheet()

    def get_rand_int_as_char(self, max_int = 10000):
        return str(random.randint(1,max_int))

    def is_image_file(self, full_path_name):
        for file_type in ("jpg", "jpeg", "png", "heic"):
            if full_path_name.lower().endswith(file_type):
                return True
        return False


    def reset_picture_dims(self):
        padw = (self.column_count - 1) * self.padding
        padh = (self.nrows - 1) * self.padding
        self.isize = (self.column_count * self.photow + self.marw + padw, self.nrows * self.photoh + self.marh + padh)
        white = (255, 255, 255)
        return Image.new('RGB', self.isize, white)

        # Iterate over the (initially) empty contact sheet image.
       


    def make_contact_sheet(self):
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

        # required for HEIC support
        register_heif_opener()

        # Set size, margins, padding
        self.photow = self.photoh = 100
        self.marl = self.mart = self.marr = self.marb = self.padding = 5
        self.marw = self.marl + self.marr
        self.marh = self.mart + self.marb

        # count the images, so we know how to arrange the rows
        # and columns
        file_list = []
        files = os.listdir(self.img_folder)
        file_count = 0
        for file in files:
            if self.is_image_file(file):
                file_count += 1
                file_list.append(file)
                if file_count > self.max_images:
                    break

        self.nrows = math.ceil(file_count/self.column_count)
        print(f"Processing [{file_count}] images")
        print(f"max_images: {self.max_images}")
        print(f"column_count: {self.column_count}")
        print(f"estimated row_count: {self.nrows}")

        contact_sheet = self.reset_picture_dims()
        icol = 0
        irow = 0

        for file in file_list:

            img_in_path = self.img_folder + "/" + file
            img = Image.open(img_in_path).resize((self.photow, self.photoh))
            left = self.marl + icol * (self.photow + self.padding)
            right = left + self.photow
            upper = self.mart + irow * (self.photoh + self.padding)
            lower = upper + self.photoh
            bbox = (left, upper, right, lower)
            contact_sheet.paste(img, bbox)
            icol += 1
            if (icol >= self.column_count):
                icol = 0
                irow += 1
                if irow % 10 == 0:
                    print(f"Processing row {irow}")
            if (irow > 20):  # create a new sheet
                srow = str(irow)
                print_file = "c:/tempx/" + "_" +  self.get_rand_int_as_char() + ".jpg"
                print(f"Contact sheet is saved as [{print_file}]")
                contact_sheet.save(print_file)
                contact_sheet = self.reset_picture_dims()
                icol = 0
                irow = 0

        print_file = "c:/tempx/" + "FinalSheet" + self.get_rand_int_as_char() + ".jpg"
        print(f"Final Contact sheet is saved as [{print_file}]")
        contact_sheet.save(print_file)
        # Done - return the contact sheet
        return contact_sheet
