"""
    Apply vfx to a clip.
    This example shows:
    1. What I choose to call a posterize effect
    2. A fadein and fadeout

    Documentation:
    ----------------
    This script applies visual effects (VFX) to a video clip using the `moviepy` library. 
    It demonstrates two effects:
    - Posterize Effect: Adjusts the color and contrast of the video.
    - Fade In and Fade Out: Adds fade-in and fade-out effects to the video.

    Dependencies:
    --------------
    - Python 3.x
    - moviepy library: Install it using `pip install moviepy`.

    File Structure:
    ----------------
    The script assumes the following directory structure relative to the `PythonSandboxAA` root folder:
    PythonSandboxAA/
    └── VideoHandling/
        └── Stitch/
            ├── test/
                ├── assets/          # Contains the input video files
                └── output/          # Stores the processed video files

    Key Variables:
    ---------------
    - SRC_ROOT: Root directory for the video handling operations.
    - ASSETS: Directory containing the input video files.
    - TARGET: Directory where the processed video files will be saved.
    - TEST_FILE: Name of the input video file to process.

    Functions:
    -----------
    main():
        - Input File: Constructs the path to the input video file using `ASSETS` and `TEST_FILE`.
        - Posterize Effect:
            - Applies a color enhancement using `vfx.colorx` with a factor of `1.5`.
            - Adjusts luminance and contrast using `vfx.lum_contrast` with parameters `(0, 50, 128)`.
            - Saves the processed video as `posterize.mp4` in the `TARGET` directory.
        - Fade In and Fade Out:
            - Adds a fade-in effect of 3 seconds using `vfx.fadein`.
            - Adds a fade-out effect of 3 seconds using `vfx.fadeout`.
            - Saves the processed video as `faders.mp4` in the `TARGET` directory.

    How to Run:
    ------------
    1. Ensure the `moviepy` library is installed.
    2. Place the input video file (`townride_no_text_10secs.mp4`) in the `assets` directory.
    3. Run the script:
       python vfx_examples01.py
    4. The processed videos will be saved in the `output` directory:
       - posterize.mp4
       - faders.mp4

    Notes:
    -------
    - Ensure the input video file exists in the `assets` directory.
    - The `output` directory must exist; otherwise, the script will throw an error.
    - Adjust the parameters of the effects as needed to customize
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
