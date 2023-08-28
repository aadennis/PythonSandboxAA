"""
POC that combines a still image and a video clip, and writes the
output to a video file.
So, if 2 video clips are cat'ed, fine.
However... if a video clip and an image clip are cat'ed, then whatever
comes second, scrolls like mad.
Docs at https://zulko.github.io/moviepy/ref/ref.html say that ImageClip
is "just" a still version of a VideoClip... but tests suggest not quite.
So in future, if I need an image and a duration as part of a larger video,
I'll use Clipchamp or similar to convert images to videos with a given
duration, and then do the concatenation.
"""
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips

CYCLE_PATH = 'c:/tempx/cycle_path.mp4'
PIANO_STILL = 'c:/tempx/piano.mp4'
CODEC = 'libx264'

OUTPUT_PATH = f'c:/tempx/cycle_with_piano_{random.randint(1,999)}.mp4'

video_clip = VideoFileClip(CYCLE_PATH)
video_clip2 = VideoFileClip(PIANO_STILL)

# Cat the 2 videos together, and write that out to file
final = concatenate_videoclips([video_clip, video_clip2])
final.write_videofile(OUTPUT_PATH,codec=CODEC,fps=30)

print(f"Image-as-video is saved at [{OUTPUT_PATH}]")
