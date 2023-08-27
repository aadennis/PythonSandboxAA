"""
    From a jpg, create a video. 
    The call (to ImageClip) must enter a duration.
    Although I have not tested this a lot, it seems the image
    must be a "proper" photo for this to convert to video. 
    So e.g. a screenshot is not working for me.
"""
from moviepy.editor import ImageClip

JPG_PATH = 'c:/tempx/piano.jpg' # save as test image
OUTPUT_PATH = 'c:/tempx/output_videox2.mp4'
DURATION=3
CODEC = 'libx264'

jpg_image = ImageClip(JPG_PATH, duration=DURATION)
jpg_image.write_videofile(OUTPUT_PATH, codec=CODEC, fps=24)
print(f"Image-as-video is saved at [{OUTPUT_PATH}]")
