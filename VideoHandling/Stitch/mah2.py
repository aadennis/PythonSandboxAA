"""
    Convert all avi files in the SRC_ROOT folder to mp4, 
    then concatenate the lot into a single mp4 file
"""
import glob
from moviepy.editor import VideoFileClip, concatenate_videoclips

SRC_ROOT = "d:/onedrive/data/photos/2023/2023_08/Bikeride to Urban Plants/"
DEST_FILE = "c:/tempx/output.mp4"

# Convert AVI files to temporary MP4 files
temp_mp4_files = []
for avi_file in glob.iglob(SRC_ROOT + "*.avi"):
    print(avi_file)
    temp_mp4_file = avi_file.replace('.avi', '_temp.mp4')
    clip = VideoFileClip(avi_file)
    clip.write_videofile(temp_mp4_file, codec='libx264')
    temp_mp4_files.append(temp_mp4_file)

# Load each temporary MP4 video clip
video_clips = [VideoFileClip(file) for file in temp_mp4_files]

final_clip = concatenate_videoclips(video_clips)
final_clip.write_videofile(DEST_FILE, codec='libx264')
