"""
    From a video, save a series of frames.
"""
from moviepy.editor import VideoFileClip, VideoClip
import numpy as np
import imageio

# SRC_ROOT = "VideoHandling/Stitch/test/" # if opened from PythonSandboxAA
SRC_ROOT = "test/"  # if opened from Stitch
ASSETS = SRC_ROOT + "assets/"
TARGET = SRC_ROOT + "output/"
TEST_FILE = "townride_no_text_10secs.mp4"

def custom_range(start,stop,step):
    current = start
    while current < stop:
        yield current
        current += step

def save_frames(input_video, start, stop, interval, output_video ):
    """
Given an input video (codec not required), and starting with the
    frame at [start] seconds, build an array, saving a frame to that array every [interval]
    seconds, stopping after [stop] seconds have been reached.
    Save the array content back to a single video file at [output_video],
    with each frame having a duration of 1.5 seconds in the video.
    """

    clip = VideoFileClip(input_video)
    frame_array = []

    for i in custom_range(start, stop, interval):
        print(i)
        frame = clip.get_frame(i)
        frame_array.append(frame)
        #imageio.imsave(f"c:/temp/xaax{i}.png", temp)

    new_clip = VideoClip(lambda t: frame_array[int(t / 1.5)], duration=(len(frame_array) * 1.5))
    new_clip.write_videofile(output_video, codec = 'libx264',fps=24)
 
if __name__ == "__main__":
    input_file = ASSETS + TEST_FILE
    start = 2.000
    stop = 9.000
    interval = 0.500
    output_file = "c:/temp/mavideo.mp4"
    save_frames(input_file, start, stop, interval, output_file)
