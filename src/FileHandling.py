"""
https://stackoverflow.com/questions/134934/display-number-with-leading-zeros
https://stackoverflow.com/questions/31375873/how-to-filter-a-list-containing-dates-according-to-the-given-start-date-and-end
https://docs.python.org/3/library/datetime.html
https://www.geeksforgeeks.org/how-to-get-file-creation-and-modification-date-or-time-in-python/
https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
https://stackoverflow.com/questions/4996405/how-do-i-change-the-file-creation-date-of-a-windows-file - difficult.
https://nitratine.net/blog/post/change-file-modification-time-in-python/
https://orthallelous.wordpress.com/2015/04/19/extracting-date-and-time-from-images-with-python/
https://newbedev.com/get-date-and-time-when-photo-was-taken-from-exif-data-using-pil
https://github.com/ianare/exif-py
https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python


handles files and folders.
"""
import argparse
from argparse import ArgumentParser
from io import FileIO
import os
import datetime
import fnmatch
from datetime import datetime
from datetime import timedelta
from os import listdir
from os.path import isfile, join
import sys
import exifread
from PIL import Image
from time import sleep, strftime
import random
import shutil

from numpy import array, source

def new_folder_for_each_month_in_year(rootb, yearb): # deprecated / redundant for a few years
    """
    asdfasdf
    """
    for i in range(1, 12 + 1):
        # to give, e.g. D:/onedrive/data/photos/_Albums/CameraRollDump/CRD_2014_01
        folder = rootb + "/CRD_{}_{:02d}".format(yearb, i)
        print(folder)
        try:
            os.mkdir(folder)
        except:
            pass

def new_folder_for_each_month_in_all_years(root): # deprecated / redundant for a few years
    for y in range(1995,2025):
        new_folder_for_each_month_in_year(root, y)

def get_files_created_between_dates(root, start_date, end_date):
    for i in listdir(root):
        filepath = os.path.join(root, i)
        filecreation_time = os.path.getctime(filepath) 
        a = datetime.fromtimestamp(filecreation_time)
        if start_date <= a <= end_date:
            print("found")
        else:
            print("not found")

def get_files_from_src_dir(rootx, target):
    ctr = 0
    DUPLICATE_LENGTH_LIMIT = 22
    for root, dirs, files in os.walk(rootx):
        for file in files:
            print("got {}-{}.".format(rootx, file))
            ctr += 1
            if ctr > 1200:
                print("reached limit of {}".format(ctr))
                return "done"
            filepath = os.path.join(rootx, file)
            text_date = get_photo_date(filepath)
            yr = text_date[0:4]
            month = text_date[5:7]
            if yr != "9999":
                sleep(0)
                folder = target + "/CRD_{}_{}".format(yr, month)
                print(folder)
                print(file)
                try:
                    new_file_path = "{}/{}".format(folder, file)
                    os.rename(filepath, new_file_path)
                except(FileExistsError):
                    if len(file) > DUPLICATE_LENGTH_LIMIT:
                        print("Duplicate found [{}]. Name > [{}] characters, so assume true duplicate. Deleting original...".format(new_file_path, DUPLICATE_LENGTH_LIMIT))
                        os.remove(filepath)
            else:
                print ("not a valid file{}".format(file))
def get_photo_date(image):
    """
    given an image, returns the date the photo was taken in this (string) format:
        2014:12:12 22:27:52 # exif
        2017-08-05 10:01:31 # fallback to modified time (created time seems a nonsense)
    """
    with open(image,'rb') as fh:
        tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal") # also "Image DateTime"
        try:
            if "EXIF DateTimeOriginal" in tags:
                a = tags["EXIF DateTimeOriginal"]
            elif "Image DateTime" in tags:
                a = tags["Image DateTime"]
            else: # no usable EXIF tags - use strftime
                # office lens jpegs etc may not have exif data - try modified date...
                filecreation_time = os.path.getmtime(image)
                txt = datetime.fromtimestamp(filecreation_time)
                return txt.strftime("%Y/%m/%d")
        except KeyError:
            print("got a KeyError")
        ax = a.values
        year = ax[0:4]
        month = ax[5:7]
        day = ax[8:10]
        
        txt = "{}/{}/{}".format(year, month, day)
        return txt


def rename_folders(root_folder):
    for y in range(1995,2025):
        for m in range(1,13):
            print("{}:{}".format(m,y))
            oldname = "{}/CRD_{:02d}_{}".format(root, m,y)
            newname = "{}/CRD_{}_{:02d}".format(root, y, m)
            print(oldname)            
            print(newname)
            try:
                os.rename(oldname, newname)
            except:
                pass

def move_all_onedrive_pictures_to_camera_roll():     
    root_folder = "D:/onedrive/Pictures"
    temp_root = "d:/temp/aaa"
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            current_file_path = "{}/{}".format(root, file)
            # new_file_path = "{}/{}/{}".format(root_folder, "Camera Roll", file)
            new_file_path = "{}/{}".format(temp_root, file)
            
            print(current_file_path)
            print(new_file_path)
            try:
                os.rename(current_file_path, new_file_path)
            except(FileExistsError):
                # quite possibly there are duplicates...
                print("Duplicate - skipping...")
                pass


def move_onedrive_pictures_to_root(root_folder = "D:/onedrive/Pictures", target = "D:/onedrive/stuff"):
    """
    The onedrive/Pictures folder contains 7 named sub-folders, a set dictated by Microsoft.
    This consolidates any content from those folders (and sub-sub-etc-folders, thanks to os.walk()),
    to a single randomly named flat folder created, by default, under  
    D:/onedrive/stuff.
    It is then up to the user, to move by hand, those files to the appropriate folder.  
    If the files are mostly from October 2021, for example, then the appropriate folder would likely  
    be D:/onedrive/stuff/CRD_2021_10. That is just based on my setup.
    You might be expecting an automation to take of distributing the files in the bucket to the 
    appropriate year-month folder. However it is easiest to sort by date descending, and move each
    month-year batch to the right folder. True for Windows at least, as OneDrive will recognise
    that they are being moved, and not complain about many files being deleted.
    """
    
    random_leaf = str(random.randint(1,999999999999999))
    target_folder = "{}/bucket_{}".format(target, random_leaf)
    os.mkdir(target_folder)
    print("Created folder [{}]".format(target_folder))

    for rootx, dirs, files in os.walk(root_folder):
        for file in files:
            src_file_path = os.path.join(rootx, file)
            target_file_path = os.path.join(target_folder, file)
            print("source folder [{}]".format(src_file_path))
            print("target folder [{}]".format(target_file_path))
            shutil.move(src_file_path, target_file_path)


def get_folders(folder: dict):
    """
    If source and desination folders are not specified on the command line, use
    defaults. You can default the source, the destination, or both.
    """
    parser = ArgumentParser(description="[Getting command line arguments]")    
    parser.add_argument("-s", "--source_folder", help="source folder: where OneDrive has saved your pictures")
    parser.add_argument("-d", "--dest_folder", help="destination folder: where to move your pictures")

    args=parser.parse_args()

    DEFAULT_SRC_DIR = "D:/onedrive/Pictures"
    DEFAULT_DEST_DIR = "D:/onedrive/Stuff"
    source_dir = ""
    dest_dir = ""

    if args.source_folder:
        source_dir = args.source_folder
    else:
        source_dir = DEFAULT_SRC_DIR

    if args.dest_folder:
        dest_dir = args.dest_folder
    else:
        dest_dir = DEFAULT_DEST_DIR


    print(f"source dir to use: [{source_dir}]")
    print(f"dest dir to use: [{dest_dir}]")

    folder['source_dir'] = source_dir
    folder['dest_dir'] = dest_dir

# entry point
if __name__ != "__main__":
    exit()

folder = {}
get_folders(folder)
print(folder['source_dir'])
print(folder['dest_dir'])

move_onedrive_pictures_to_root(folder['source_dir'], folder['dest_dir'])
