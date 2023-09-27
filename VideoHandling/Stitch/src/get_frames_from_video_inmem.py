"""
    From a video, get a series of frames.
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
    """
        Python Range accepts only integers. This supports floats.
    """
    current = start
    while current < stop:
        yield current
        current += step

def get_frames(input_video, frame_start, frame_stop, frame_interval):
    """
    Given an input video (codec not required), and starting with the
    frame at [start] seconds, build an array, saving a frame to that array every [interval]
    seconds, stopping after [stop] seconds have been reached.
    Save the array content back to a single video file at [output_video],
    with each frame having a duration of 1.01 seconds in the video.
    """

    clip = VideoFileClip(input_video)
    frame_array = []

    for i in custom_range(frame_start, frame_stop, frame_interval):
        frame = clip.get_frame(i)
        frame_array.append(frame)

    new_clip = VideoClip(lambda t: frame_array[int(t / 1.01)], duration=(len(frame_array) * 1.01))
    return new_clip
 
if __name__ == "__main__":
   

    # Next is a 2 second (stop) video with frames at 0.091 seconds.
    input_file = r'E:\Den\VideoDump\GolfVideos\ActionCamera\golf_range_18_09_2023\joined\golf_range_18_09_2023.mp4'
    start = (20 * 60) + 9
    stop = start + 2
    interval = 0.091
    output_file = "c:/temp/mavideox.mp4"

    ans = get_frames(input_file, start, stop, interval)
    ans.write_videofile(output_file, codec = 'libx264',fps=24)
    print(ans)
