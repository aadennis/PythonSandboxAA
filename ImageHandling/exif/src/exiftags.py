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

import subprocess
from sys import platform
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


    def set_tag_set(self, tag_set):
        """
        Add a tag, or a set of tags to the file passed to the ctor.
        Any existing tags are truncated.
        todo: rn this truncates existing tags - needs to just add unless
        truncate has been requested.
        For now, we run get_tag_set, and if the file has tags, we
        raise an exception and exit, else we write.
        """
        current_tag_set = self.get_tag_set()
        if current_tag_set != self.NO_TAGS:
            print(f"Current: {current_tag_set}")
            print(f"no tags: {self.NO_TAGS}")
            raise AssertionError(f"[{self.image_file}] already has a tag set. Exiting...")
        write_args=[self.EXIF_TOOL_NAME,f"-Subject={tag_set}", self.image_file]
        response = self.run_subprocess(args_for_subprocess=write_args)
        if not response ==  self.WRITE_SUCCESS:
            raise AssertionError(f"Expected {self.WRITE_SUCCESS}, Got {response}")
        return self.SUCCESS


    def get_tag_set(self):
        """
        Read back the set of tags for the file passed to the ctor.
        This is also useful for checking that the write went ok.
        """
        read_args=[self.EXIF_TOOL_NAME,"-Subject", self.image_file]
        return self.run_subprocess(args_for_subprocess=read_args)

    # pylint: disable=R0201
    def run_subprocess(self, args_for_subprocess):
        """
            Execute subprocess.check_output().
            This is a separate method to allow mocking and to avoid needing to
            commit 3rd party software to Github just to allow testing by
            Actions.
            todo - move to utilities
        """
        return str(subprocess.check_output(args=args_for_subprocess))
