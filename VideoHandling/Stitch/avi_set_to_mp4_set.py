"""
    Convert all avi files in the SRC_ROOT folder to mp4
"""
import glob
from moviepy.editor import VideoFileClip 

SRC_ROOT = "E:\\Den\\YoutubeMasters\\ToMatford\\Originals\\VIDEO/"
DEST_FILE = "E:\\Den\\YoutubeMasters\\ToMatford\\Originals\\AviFormat"

# Convert AVI files to MP4 files
for avi_file in glob.iglob(SRC_ROOT + "*.avi"):
    print(avi_file)
    temp_mp4_file = avi_file.replace('.avi', '_temp.mp4')
    clip = VideoFileClip(avi_file)
    clip.write_videofile(temp_mp4_file, codec='libx264')
