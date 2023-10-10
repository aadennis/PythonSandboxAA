"""
From an mp4, extract a clip.
In this example, I take from 50 seconds in to 1 minute,
that is, 10 seconds-worth
https://moviepy.readthedocs.io/en/latest/getting_started/quick_presentation.html#example-code
"""

from moviepy.editor import VideoFileClip
from moviepy import *

START_CLIP = "00:02:55"
END_CLIP = "00:03:30"

INPUT_VIDEO = r"C:\VideoStaging\Sea 25-09-2023\Sea_25-09-2023.mp4"
# also webm, etc. But note that mp4 for 10 seconds in this consumes 10mb, that is
# 1mb per second. webm uses only 2mb, so 20% of the mp4.
OUTPUT_VIDEO = r"C:\VideoStaging\Sea 25-09-2023\Sea_25-09-2023_short1.mp4" 

CLIP = VideoFileClip(INPUT_VIDEO).subclip(START_CLIP, END_CLIP)
CLIP.write_videofile(OUTPUT_VIDEO)
