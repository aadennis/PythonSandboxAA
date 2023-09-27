"""
    From a single jpg, create a video. 
    The call (to ImageClip) must enter a duration.
    Note that if your source for the image is originally
    a .heic file, then use Irfanview to do the save-as, else
    if you use e.g. MS Photos you might get "bad codec" type-
    thing.
    Screenshots saved as jpg: I have found this is a bit inconsistent:
    sometimes it works fine, sometimes "...won't play". 
"""
from moviepy.editor import ImageClip

JPG_PATH = 'c:/tempx/pah.jpg'
OUTPUT_PATH = 'c:/tempx/pah.mp4'
DURATION=6
CODEC = 'libx264'
#CODEC = 'mpeg4'

jpg_image = ImageClip(JPG_PATH, duration=DURATION)
jpg_image.write_videofile(OUTPUT_PATH, codec=CODEC, fps=24)
print(f"Image-as-video is saved at [{OUTPUT_PATH}]")
