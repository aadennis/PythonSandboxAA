"""
    From a video, save a single frame.
    You specify the position of the frame in the video
    in seconds, as a float.


"""
from moviepy.editor import *
from moviepy import video

# SRC_ROOT = "VideoHandling/Stitch/test/" # if opened from PythonSandboxAA
SRC_ROOT = "test/"  # if opened from Stitch
ASSETS = SRC_ROOT + "assets/"
TARGET = SRC_ROOT + "output/"
TEST_FILE = "townride_no_text_10secs.mp4"


def save_a_frame(input_video, output_video, frame_position):
    """
    Given an input video (codec not required), save a frame
    at frame_position seconds to output_file
    """
    clip = VideoFileClip(input_video)
    clip.save_frame(output_video, frame_position)


if __name__ == "__main__":
    input_file = ASSETS + TEST_FILE
    output_file = "c:/temp/mah2ux.png"
    frame = 8.532
    save_a_frame(input_file, output_file, frame)
