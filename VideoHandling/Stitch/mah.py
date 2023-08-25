from moviepy.editor import VideoFileClip, concatenate_videoclips

# List of AVI file paths
src_root = "c:/temp/"
dest_root = "c:/tempx/"
avi_files = [src_root + 'MOVI0000.avi',src_root + 'MOVI0002.avi' ]

from pathlib import Path 
print("File Path:", Path(__file__).absolute()) 
print("Directory Path:", Path().absolute()) # Directory of current working directory, not __file__


# Load each video clip
video_clips = [VideoFileClip(file) for file in avi_files]

# Concatenate the video clips
final_clip = concatenate_videoclips(video_clips)

# Write the final concatenated video to a file
final_clip.write_videofile('c:/tempx/out.avi', codec='XVID') # MJPG rawvideo

