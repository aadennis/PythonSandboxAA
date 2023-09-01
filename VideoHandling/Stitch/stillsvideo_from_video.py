"""
    Given a single video in mp4 format, 
    at frame_interval intervals (see below), 
    write the frame found at the interval to
    an mp4 file, holding the frame frame_display_duration 
    seconds. 
"""

from moviepy.editor import VideoFileClip, VideoClip

def process_frame(t, get_frame_func):
    """
        todo docs
    """
    frame_time = int(t)
    frame = get_frame_func(frame_time)
    return frame

def main():
    """
        todo fix
        IndexError: list index out of range
        The file still writes, but debug the cause.
    """
    input_video = "E:\\Den\\VideoDump\\VideoAssets\\13second_test_vid.mp4"
    output_video = "E:\\Den\\VideoDump\\VideoAssets\\delayed_frames.mp4"
    frame_interval = 2
    frame_display_duration = 1

    video_clip = VideoFileClip(input_video)
    fps = video_clip.fps
    duration = video_clip.duration

    def get_frame_at_time(time):
        return video_clip.get_frame(time)
    
    new_frames = []
    for t in range(0, int(duration), frame_interval):
        frame = process_frame(t, get_frame_at_time)
        new_frames.extend([frame] * int(frame_display_duration * fps))

    new_video_clip = VideoClip(lambda t: new_frames[int(t * fps)], duration = duration)
    new_video_clip.fps = fps

    new_video_clip.write_videofile(output_video, codec="libx264")

if __name__ == "__main__":
    main()
