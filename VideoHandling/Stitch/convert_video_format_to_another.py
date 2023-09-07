"""
    Convert all video files of one format to another format
"""
import os
import glob
from moviepy.editor import VideoFileClip

SRC_ROOT = "VideoHandling/Stitch/test/" # generally relative to PythonSandboxAA
ASSETS = SRC_ROOT + "assets/"
TARGET = SRC_ROOT + "output/"
SOURCE_WILD_CARD = "bof*"
SOURCE_FILE_TYPE = ".mp4"
TARGET_FILE_TYPE = ".avi"
CODEC = 'libx264'

def get_filename_no_ext(path):
    """
        Given a full path name, return just the filename, 
        without its extension.
        For example, "c:/temp/test.txt" returns "test"
    """
    return os.path.splitext(os.path.basename(path))[0]

def main():
    found = False
    for file in glob.iglob(ASSETS + SOURCE_WILD_CARD + SOURCE_FILE_TYPE):
        found = True
        filename = get_filename_no_ext(file)
        avi_file = TARGET + filename + TARGET_FILE_TYPE
        clip = VideoFileClip(file)
        clip.write_videofile(avi_file, codec=CODEC)
    if not found:
        raise Exception(FileNotFoundError, "No source files were found:[" + ASSETS + "]")

if __name__ == "__main__":
    main()
