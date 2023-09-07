"""
    Convert all video files of one format to another format
"""
import os
import glob
from moviepy.editor import VideoFileClip

SRC_ROOT = "d:/Sandbox/git/aadennis/PythonSandboxAA/VideoHandling/Stitch/test/"
ASSETS = SRC_ROOT + "assets/"
TARGET = SRC_ROOT + "output/"
SOURCE_WILD_CARD = "bof*.mp4"


def get_filename_no_ext(path):
    """
        Given a full path name, return just the filename, 
        without its extension.
        For example, "c:/temp/test.txt" returns "test"
    """
    return os.path.splitext(os.path.basename(path))[0]

# Convert mp4 files to avi format
for file in glob.iglob(ASSETS + SOURCE_WILD_CARD):
    filename = get_filename_no_ext(file)
    avi_file = TARGET + filename + ".avi"
    clip = VideoFileClip(file)
    clip.write_videofile(avi_file, codec='libx264')
