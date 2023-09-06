"""
From an mp4, extract a clip.
In this example, I take from 50 seconds in to 1 minute,
that is, 10 seconds-worth
https://moviepy.readthedocs.io/en/latest/getting_started/quick_presentation.html#example-code
"""

from moviepy.editor import VideoFileClip
from moviepy import *

INPUT_VIDEO = "c:/VideoStaging/mp4Joined.mp4"
# also webm, etc. But note that mp4 for 10 seconds in this consumes 10mb, that is
# 1mb per second. webm uses only 2mb, so 20% of the mp4.
OUTPUT_VIDEO = "c:/VideoStaging/shorty.mp4" 

clip = VideoFileClip(INPUT_VIDEO).subclip("00:00:50","00:01:00")

clip.write_videofile(OUTPUT_VIDEO)
