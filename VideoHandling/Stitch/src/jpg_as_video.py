"""
    From a single jpg, create a video. 
    The call (to ImageClip) must enter a duration.
    Although I have not tested this a lot, it seems the image
    must be a "proper" photo for this to convert to video. 
    So e.g. a screenshot is not working for me.
"""
from pathlib import Path
from moviepy.editor import ImageClip

JPG_PATH = 'VideoHandling/Stitch/test/assets/piano.jpg'
OUTPUT_PATH = 'VideoHandling/Stitch/test/output/piano.mp4'
DURATION=3
CODEC = 'libx264'

jpg_image = ImageClip(JPG_PATH, duration=DURATION)
jpg_image.write_videofile(OUTPUT_PATH, codec=CODEC, fps=24)
print(f"Image-as-video is saved at [{OUTPUT_PATH}]")
