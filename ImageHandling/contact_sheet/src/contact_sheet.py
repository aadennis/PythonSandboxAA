# Credit for original: https://code.activestate.com/recipes/ (join lines)
# 578267-use-pil-to-make-a-contact-sheet-montage-of-images/
import os
import glob
import random
import math
from PIL import Image
from pillow_heif import register_heif_opener
from datetime import datetime

class ContactSheet:

    def __init__(self, img_folder,  max_images=100, column_count=3):
        self.img_folder = img_folder
        self.max_images = max_images
        self.column_count = column_count
        self.max_rows_per_page = 10
        self.image_count = None # not known at this point
        self.make_contact_sheet()

    def get_max_rows_per_page(self):
        min_comp = min(self.total_rows_available, self.max_rows_per_page)
        self.total_images_remaining -= (min_comp * self.column_count)
        self.total_rows_available = int(self.total_images_remaining / self.column_count)
        return min_comp

    def get_rand_int_as_char(self, max_int = 10000):
        return str(random.randint(1,max_int))

    def is_image_file(self, full_path_name):
        for file_type in ("jpg", "jpeg", "png", "heic"):
            if full_path_name.lower().endswith(file_type):
                return True
        return False


    def reset_picture_dims(self):
        padw = (self.column_count - 1) * self.padding
        padh = (self.total_rows_available - 1) * self.padding
        contact_sheet_width = int(self.column_count * self.photow + self.marw + padw)
        contact_sheet_length = int(self.get_max_rows_per_page() * self.photoh + self.marh + padh)
        print(f"contact_sheet_width: {contact_sheet_width}")
        print(f"contact_sheet_length: {contact_sheet_length}")
        
        self.isize = (contact_sheet_width,  contact_sheet_length)
        white = (255, 255, 255)
        # https://pillow.readthedocs.io/en/stable/reference/Image.html#constructing-images
        return Image.new('RGB', self.isize, white)

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

        now = datetime.now()
        self.file_name_root = now.strftime('contactsheet-%H-%M-%S-pt')
        self.file_part = 1

        # Set size, margins, padding
        self.photow = self.photoh = 100
        self.marl = self.mart = self.marr = self.marb = self.padding = 5
        self.marw = self.marl + self.marr
        self.marh = self.mart + self.marb

        # count the images, so we know how to arrange the rows
        # and columns
        file_list = []
        files = os.listdir(self.img_folder)
        self.image_count = 0
        for file in files:
            if self.is_image_file(file):
                self.image_count += 1
                file_list.append(file)
                if self.image_count > self.max_images:
                    break
        self.total_rows_available = int(self.image_count/self.column_count)
        self.total_images_remaining = self.total_rows_available * self.column_count

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
            if (irow > self.max_rows_per_page):  # create a new sheet
                print_file = "c:/tempx/" + self.file_name_root + str(self.file_part) + ".jpg"
                self.file_part += 1
                print(f"Contact sheet is saved as [{print_file}]")
                contact_sheet.save(print_file)
                contact_sheet = self.reset_picture_dims()
                icol = 0
                irow = 0

        print_file = "c:/tempx/" + self.file_name_root + str(self.file_part) + ".jpg"
        self.file_part += 1
        print(f"Final Contact sheet is saved as [{print_file}]")
        contact_sheet.save(print_file)
        # Done - return the contact sheet
        return contact_sheet
