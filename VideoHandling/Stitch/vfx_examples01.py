"""
    Apply vfx to a clip.
    This example shows 
    1. What I choose to call a posterize effect
    2. A fadein and fadeout
"""
from moviepy.editor import VideoFileClip, vfx

SRC_ROOT = "VideoHandling/Stitch/test/" # generally relative to PythonSandboxAA
ASSETS = SRC_ROOT + "assets/"
TARGET = SRC_ROOT + "output/"
TEST_FILE = "townride_no_text_10secs.mp4"

def main():
    file = ASSETS + TEST_FILE
    clip = VideoFileClip(file)
    posterize_clip = clip.fx(vfx.colorx, 1.5).fx(vfx.lum_contrast, 0,50,128)
    posterize_clip.write_videofile(TARGET + "posterize.mp4")
    fadeinout_clip = clip.fx(vfx.fadein, 3).fx(vfx.fadeout, 3)
    fadeinout_clip.write_videofile(TARGET + "faders.mp4")            
   
if __name__ == "__main__":
    main()
