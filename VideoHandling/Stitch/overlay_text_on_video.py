"""
Given a video file as input, create a copy that
includes a title up to n seconds before the end 
of the source version.
"""

from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

INPUT_VIDEO = "c:/VideoStaging/shorty_no_text.mp4"
OUTPUT_VIDEO = "c:/VideoStaging/shorty_with_text.mp4" 

video_clip = VideoFileClip(INPUT_VIDEO)

txt_clip = TextClip("Exmouth to Exeter - 08.2023",fontsize=70,color="black", bg_color="white")
# set_position: there are various overloads. This one shows 
# set_position((0.00001,0.3) = text (more actually background) 0.001% from the left,
#  and top edge 0.001% from top 
# duration: the text will play the entirety of the video clip, but not the last 5
# seconds ()  set_duration(clip.duration - 5)
# Note that it does not assign text dynamically. So if you ask for an offset for argument 1 of 0.5, 
# and there is not enough space for your text, it will just chuck the right hand bit off to the side
# - the trailing part will not be visible
txt_clip = txt_clip.set_position((0.5,0.1),relative=True).set_duration(video_clip.duration - 5)
video = CompositeVideoClip([video_clip, txt_clip])
video.write_videofile(OUTPUT_VIDEO)
