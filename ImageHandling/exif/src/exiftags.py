"""
This is just a wrapper around the fantastic exiftool written by Phil Harvey.
See here for the source:
https://github.com/exiftool
and here for chapter and verse:
https://www.exiftool.org/
The exiftool executables are not checked in. So when you deploy, follow the
instructions in readme.md (todo).
Testing on Github Actions uses mocks.
"""


from sys import platform
import glob
import os
from datetime import datetime
from Utilities.src.utility import Utility


class ExifTags():
    """
    Manage the exif tags of a single file.
    The tags of interest are specifically those called "Subject tags",
    which OneDrive exposes just as Tags, e.g. #dog, e.g. #car.
    """

    if platform == 'win32':
        WRITE_SUCCESS = "b'    1 image files updated\\r\\n'"
        EXIF_TOOL_NAME = "PythonSandbox/ImageHandling/exif/third_party/exiftool.exe"
    else: # linux
        WRITE_SUCCESS = "b'    1 image files updated\\n'"
        EXIF_TOOL_NAME = "ImageHandling/exif/third_party/Image-ExifTool-12.37/exiftool"

    SUCCESS = 0
    NO_TAGS = "b''"

    def __init__(self, image_file):
        # all subsequent methods depend on this file
        Utility().file_exists(image_file)
        self.image_file = image_file

    def write_tags(self, tag_set):
        write_args=[self.EXIF_TOOL_NAME,f"-Subject={tag_set}", self.image_file]
        response = Utility().run_subprocess(args_for_subprocess=write_args)
        if not response ==  self.WRITE_SUCCESS:
            raise AssertionError(f"Expected {self.WRITE_SUCCESS}, Got {response}")
        return self.SUCCESS


    def set_tag_set(self, tag_set, additional_tags='N'):
        """
        Add a tag, or a set of tags to the file passed to the ctor.
        Default is that you cannot add tags if the file already has
        tag(s) (additional_tags='N')
        Additional tags will only be added if Y is passed, given the
        danger of a bulk update resulting in an unintended overwrite.
        """
        current_tag_set = self.get_tag_set()
        if current_tag_set != self.NO_TAGS:
            print(f"Current: {current_tag_set}")
            print(f"no tags: {self.NO_TAGS}")
            
            if additional_tags != 'Y':
                raise AssertionError(f"[{self.image_file}] already has a tag set. Exiting...")
            # additional tags...
            updated_tag_set = f"{tag_set};{current_tag_set}"
            updated_tag_set = updated_tag_set.replace(self.NO_TAGS,"")
            self.write_tags(updated_tag_set)
            
        else: # no existing tags
          self.write_tags(tag_set)
        return self.SUCCESS

    def get_tag_set(self):
        """
        Read back the set of tags for the file passed to the ctor.
        This is also useful for checking that the write went ok.
        """
        read_args=[self.EXIF_TOOL_NAME,"-Subject", self.image_file]
        tag_set = Utility().run_subprocess(args_for_subprocess=read_args)
        print(f"a. where we are: {tag_set}")
        a = tag_set.replace("b'Subject                         :","").replace("\\n'","")
        print(f"b. where we are: {a}")
        return a



    def get_photo_date(self):
        """
        given an image, returns the date the photo was taken, using these rules:
            if exif available, use that (case 1)
            else if Image DateTime available, use that (case 2)
            else use the modified date (case 3)
            Formats:
            case 1 - exif: 2014:12:12 22:27:52 
            case 2 - exif: 2014:12:12 22:27:52
            case 3 - modified time fallback: 2017-08-05 10:01:31 
                (created time seems a nonsense)
        """
        #with open(self.image,'rb') as fh:
        read_args=[self.EXIF_TOOL_NAME,"-DateTimeOriginal", self.image_file] 
        print(f"file name:{self.image_file}")
        tags = Utility().run_subprocess(args_for_subprocess=read_args)
        #tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal") # also "Image DateTime"
        try:
            if "EXIF DateTimeOriginal" in tags:
                a = tags["EXIF DateTimeOriginal"]
            elif "Image DateTime" in tags:
                a = tags["Image DateTime"]
            else: # no usable EXIF tags - use strftime
                # office lens jpegs etc may not have exif data - try modified date...
                filecreation_time = os.path.getmtime(self.image_file)
                txt = datetime.fromtimestamp(filecreation_time)
                return txt.strftime("%Y/%m/%d")
        except KeyError:
            print("got a KeyError")
        ax = a.values
        year = ax[0:4]
        month = ax[5:7]
        day = ax[8:10]
        
        txt = "{}/{}/{}".format(year, month, day)
        print(txt)
        return txt


class ExifTagsList():
    """
    Handler for a set of files in a single directory, on which EXIF actions
    are to be performed.
    Only supports jpg rn.
    See class ExifTags for actions performed on the files within each iteration.
    """
    def __init__(self, image_folder, tag_set, append_ok = "N"):
        # all subsequent methods depend on this folder
        fileList = []
        folder = f'{image_folder}/*.jpg'
        for filepath in glob.iglob(folder):
            e_t = ExifTags(filepath)
            e_t.set_tag_set(tag_set, append_ok)
            print(filepath)



if __name__ == '__main__':
    tag_set = "trawler;fishing"
    append_ok = "Y"
    etl = ExifTagsList("/tmp/work", tag_set, append_ok)
