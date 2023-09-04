"""
From an mp4, extract a clip.
In this example, I take from 50 seconds in to 1 minute,
that is, 10 seconds-worth.
Also put some text in as an overlay.
https://moviepy.readthedocs.io/en/latest/getting_started/quick_presentation.html#example-code
"""

from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

INPUT_VIDEO = "c:/VideoStaging/mp4Joined.mp4"
# also webm, etc. But note that mp4 for 10 seconds in this consumes 10mb, that is
# 1mb per second. webm uses only 2mb, so 20% of the mp4.
# Also note that it evidently dynamically parses the extension, as INPUT_VIDEO works 
# for .mp4 without me changing anything, and also .webm.
OUTPUT_VIDEO = "c:/VideoStaging/shorty.mp4" 

video_clip_set = []
video_clip_set.append(VideoFileClip(INPUT_VIDEO).subclip("00:00:50","00:01:00"))


txt_clip = TextClip("Exmouth to Exeter - 08.2023",fontsize=70,color="black", bg_color="white")
# set_position: there are various overloads. This one shows 
# set_position((0.00001,0.3) = text (more actually background) 0.001% from the left,
#  and top edge 0.001% from top 
# duration: the text will play the entirety of the video clip, but not the last 5
# seconds ()  set_duration(clip.duration - 5)
# Note that it does not assign text dynamically. So if you ask for an offset for argument 1 of 0.5, 
# and there is not enough space for your text, it will just chuck the right hand bit off to the side
# - the trailing part will not be visible

txt_clip = txt_clip.set_position((0.5,0.1),relative=True).set_duration(5)
video = CompositeVideoClip([video_clip_set[0], txt_clip])
video.write_videofile(OUTPUT_VIDEO)
