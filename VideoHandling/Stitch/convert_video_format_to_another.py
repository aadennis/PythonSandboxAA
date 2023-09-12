"""
    Convert all video files of one format to another format
"""
import os
import glob
from pathlib import Path
from moviepy.editor import VideoFileClip

SRC_ROOT = "test/"  # relative to current root
ASSETS = SRC_ROOT + "assets/"
TARGET = SRC_ROOT + "output/"
SOURCE_WILD_CARD = "bof*"
CODEC = 'libx264'


def get_filename_no_ext(path):
    """
        Given a full path name, return just the filename, 
        without its extension.
        For example, "c:/temp/test.txt" returns "test"
    """
    return os.path.splitext(os.path.basename(path))[0]

def get_arbitrary_extension(path, wildcard = None):
    """
        Given the full path to a folder, return 
        just the extension of an arbitrary file
        For example, if "c:/temp/" contains files of 
        extension ".txt" and ".doc", it may return txt or doc
        (but not both).
        wildcard: this restricts deciding on the arbitrary extension
    """
    first_file = glob.glob(os.path.join(path, wildcard))[0]
    return os.path.splitext(first_file)[1]
    # return os.path.splitext(os.path.basename(path))[0]

def convert_video_format(target_format, wildcard, src_folder=None):
    """
        Convert all video files of one format to another format.
        src_folder must contain only one type of video file. 
        For example, all .avi or all .mp4 etc. It assumes that 
        is the source format.
        target_format: the extension for the format to which 
        the video is to be converted. You must include ".". for
        example: .avi and not avi
        Wildcard: especially for testing, there might be a mix of 
        filenames, e.g "MyHouse123", "MyHouse345", "MyGarden123".
        If you only want House videos, enter "MyHouse*". If you want all files,
        enter None
    """
    if src_folder is None:
        src_folder = ASSETS

    if wildcard is None:
        wildcard = ""
    
    source_file_type = get_arbitrary_extension(src_folder, wildcard)
    print(f"src_folder is is is: {src_folder}")
    print(f"Source file type is is is {source_file_type}")
    found = False


    
    for file in glob.iglob(src_folder + wildcard + source_file_type):
        found = True
        print(f"Converting source file: {file}")
        filename = get_filename_no_ext(file)
        avi_file = TARGET + filename + target_format
        clip = VideoFileClip(file)
        clip.write_videofile(avi_file, codec=CODEC)
    if not found:
        print("***** Root folder when searching for assets:",
              Path().absolute(), " **********")
        raise Exception(FileNotFoundError,
                        "No source files were found:[" + ASSETS + "]")


if __name__ == "__main__":
    src_folder = r"C:\VideoStaging\shopping_trip"
    # get_arbitrary_extension(src_folder)
    convert_video_format(".avi", "bof*") #, src_folder)
