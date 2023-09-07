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

# Convert mp4 files to avi format
for mp4_file in glob.iglob(ASSETS + SOURCE_WILD_CARD):
    print(mp4_file)
    a = os.path.basename(mp4_file)
    print(a)
    b = os.path.splitext(a)[0]
    print(b)
    avi_file = TARGET + b + ".avi"
    print(avi_file)
    clip = VideoFileClip(mp4_file)
    clip.write_videofile(avi_file, codec='libx264')
