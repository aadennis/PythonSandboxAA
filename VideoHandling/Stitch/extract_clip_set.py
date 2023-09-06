"""
    From a video file, every i seconds, write a 10 second clip
    to a new video file (a single file, not one for each 10
    second clip).
"""
from moviepy.editor import VideoFileClip, concatenate_videoclips

INPUT_VIDEO = "c:/VideoStaging/mp4Joined.mp4"
OUTPUT_VIDEO = "c:/VideoStaging/shorty.mp4" 

video_clip_set = []

for i in range(0,500,60):
    print(i)
    video_clip_set.append(VideoFileClip(INPUT_VIDEO).subclip(i,i+10))

final_clip = concatenate_videoclips(video_clip_set, method="compose")
final_clip.write_videofile(OUTPUT_VIDEO, codec='libx264')
