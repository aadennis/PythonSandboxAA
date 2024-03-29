"""
    Convert all video files of one format to another format.
    09.2023: I know it can support a source of avi or mov,
    and a target of avi or mp4.
    Other formats / directions not yet tested
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
    try: 
        files = path + "/" + wildcard 
        first_file = glob.glob(files)[0]
    except IndexError as exc:
        #https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/raise-missing-from.html#raise-missing-from-w0707
        msg = f"No items found for [{path}] with wildcard [{wildcard}]"
        print(msg)
        raise msg from exc

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
        Examples:
        convert_video_format(".mp4", wildcard=None, src_folder=SRC_FOLDER)
    """
    if src_folder is None:
        src_folder = ASSETS

    if wildcard is None:
        wildcard = "*"
    
    source_file_type = get_arbitrary_extension(src_folder, wildcard)
    print(f"src_folder is is is: {src_folder}")
    print(f"Source file type is is is {source_file_type}")
    found = False

    joined_path = src_folder + "/" + wildcard + source_file_type
    for file in glob.iglob(joined_path):
        found = True
        print(f"Converting source file: {file}")
        filename = get_filename_no_ext(file)
        converted_file = TARGET + filename + target_format
        clip = VideoFileClip(file)
        clip.write_videofile(converted_file, codec=CODEC)
    if not found:
        print("***** Root folder when searching for assets:",
              Path().absolute(), " **********")
        raise Exception(FileNotFoundError,
                        "No source files were found:[" + ASSETS + "]")


if __name__ == "__main__":
    # Example 1 - target is avi, source files have the name mp4_bof*,
    # source folder contains a mix of mp4 and avi, but the wildcard
    # restricts to mp4.
    # src_folder is determined in the code, given None here
    #convert_video_format(".avi", "mp4_bof*", src_folder=None)
    
    # Example 2 - target is mp4, source folder contains all avi or mov files
    # (moviepy deals with that), don't restrict to a wildcard filename
    SRC_FOLDER = r"C:\VideoStaging\USB Drive\Sea swim 09.10.2023"
    convert_video_format(".mp4", wildcard=None, src_folder=SRC_FOLDER)
