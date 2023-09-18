"""
    From a video, save a series of frames.
"""
from moviepy.editor import VideoFileClip
import numpy as np
import imageio

# SRC_ROOT = "VideoHandling/Stitch/test/" # if opened from PythonSandboxAA
SRC_ROOT = "test/"  # if opened from Stitch
ASSETS = SRC_ROOT + "assets/"
TARGET = SRC_ROOT + "output/"
TEST_FILE = "townride_no_text_10secs.mp4"

# def custom_range(start,stop,interval):
#     current = start
#     while current < stoi

def save_frames(input_video, start, stop, interval ):
    """
    Given an input video (codec not required), and starting with the
    frame at [start] seconds, save a frame to png every [interval]
    seconds, stopping after [frame_count] images have been saved.
    """

    clip = VideoFileClip(input_video)

    for i in range(start, stop, interval):
        print(i)
        temp = clip.get_frame(i)
        imageio.imsave(f"c:/temp/aax{i}.png", temp)


    # a = clip.get_frame(1.001)
    # b.append(a)
    # a = clip.get_frame(2.001)
    # print(type(a))
    # b.append(a)

    # for seq, val in enumerate(b):
    #     imageio.imsave(f"c:/temp/aa{seq}.png", val)
    
    #clip.save_frame(output_video, frame_position)

 
if __name__ == "__main__":
    input_file = ASSETS + TEST_FILE
    start = 2 #.000
    stop = 9 #.000
    interval = 1 #.000
    save_frames(input_file, start, stop, interval)
