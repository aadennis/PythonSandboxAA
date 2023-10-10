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


def custom_range(start, stop, step):
    """
        Python Range accepts only integers. This supports floats.
    """
    current = start
    while current < stop:
        yield current
        current += step


def get_frames_from_video(input_video, frame_start, frame_stop, frame_interval, frame_display_duration = 2):
    """
    Given an input video (codec not required), the first frame to grab is at 
    [frame_start] seconds. The last frame to grab is at [frame_start] + [frame_stop]
    seconds. Between those 2 boundaries, grab a frame every [frame_interval] seconds.
    As an example, say input_video has a duration of 120 seconds. The range from which 
    I want to select my frames between a) 40 seconds from the start of input_video, 
    and b) 70 seconds from the start of input_video.
    That requires a frame_start value of 40 seconds, and a frame_stop value of 30
    seconds (40 + 30).
    Within that, I want a frame to be grabbed every 10.7 seconds. So frame_interval is
    10.7. 
    If I want each frame to be displayed for 2.3 seconds, frame_display_duration is 2.3.
    The return type is a VideoClip. It is not a VideoFileClip, as something else should
    own that file writing.
    """

    clip = VideoFileClip(input_video)
    frame_array = []

    for i in custom_range(frame_start, frame_stop, frame_interval):
        frame = clip.get_frame(i)
        frame_array.append(frame)

    new_clip = VideoClip(lambda t: frame_array[int(
        t / frame_display_duration)], duration=(len(frame_array) * frame_display_duration))
    return new_clip


if __name__ == "__main__":

    # Next is a 2 second (stop) video with frames at 0.091 seconds.
    input_file = r'D:\Sandbox\git\aadennis\PythonSandboxAA\VideoHandling\Stitch\test\assets\Sea swim 1m45.mp4'
    start = 20 # seconds
    stop = start + 40
    interval = 1
    output_file = "c:/temp/mavideox.mp4"


    ans = get_frames_from_video(input_file, start, stop, interval)
    ans.write_videofile(output_file, codec='libx264', fps=24)
    print(ans)
