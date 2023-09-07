"""
    Convert all video files of one format to another format
"""
import glob
from moviepy.editor import VideoFileClip

SRC_ROOT = "d:/Sandbox/git/aadennis/PythonSandboxAA/VideoHandling/Stitch/test/assets/"

# Convert mp4 files to avi format
for mp4_file in glob.iglob(SRC_ROOT + "bof*.mp4"):
    print(mp4_file)
    avi_file = mp4_file.replace('.mp4', '.avi')
    clip = VideoFileClip(mp4_file)
    clip.write_videofile(avi_file, codec='libx264')
