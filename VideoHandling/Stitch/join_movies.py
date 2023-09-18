"""
    Given a set of video clips in mp4 format, 
    concatenate the lot into a single mp4 file.
"""
import glob
from moviepy.editor import VideoFileClip, concatenate_videoclips

SRC_ROOT = r"C:\VideoStaging\ActionCamera\output/"
DEST_FILE = r"C:\VideoStaging\ActionCamera\temp\\golf_range_18_09_2023.mp4"

temp_mp4_files = sorted(glob.iglob(SRC_ROOT + "*.mp4"))
for i in temp_mp4_files:
    print(i)

video_clips = [VideoFileClip(file) for file in temp_mp4_files]

final_clip = concatenate_videoclips(video_clips)
final_clip.write_videofile(DEST_FILE, codec='libx264')

