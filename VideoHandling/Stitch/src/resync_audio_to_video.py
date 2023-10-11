"""
    Fix audio vs video sync issues.
"""
from moviepy.editor import VideoFileClip

# SRC_ROOT = "VideoHandling/Stitch/test/" # if opened from PythonSandboxAA
SRC_ROOT = "test/"  # if opened from Stitch
ASSETS = SRC_ROOT + "assets/"
TARGET = SRC_ROOT + "output/"
TEST_FILE = "townride_no_text_10secs.mp4"

def resync(input_video, time_offset):
    """
    Summary: Resync audio with video. Basically sort lip-sync timing issues.
    Detail: Audio may lag on a cheap action camera. And even given the same
    camera, the lag may vary between 0 and say 2 seconds.
    A plus value for time_offset puts the audio ahead of a (synced) video.
    """

    video_clip = VideoFileClip(input_video)
    video = video_clip.subclip(0, video_clip.duration - time_offset)
    audio = video_clip.audio.subclip(max(0, time_offset), video_clip.duration)
    video = video.set_audio(audio)

    return video

def resync_audio_to_video(input_file, output_file, time_offset = 1):
    """
        See [get_frames_from_video] for full description.
        Call get_frames_from_video, passing through the same parameters.
        Write the returned VideoClip to a file
    """
    frame_set = resync(input_file, time_offset)
    frame_set.write_videofile(output_file, codec='libx264', fps=24)


if __name__ == "__main__":

    test_input_file = ASSETS + '/golf_out_of_sync_audio.mp4'
    #test_input_file = ASSETS + '/lip_sync_ok.MOV'
    test_output_file = "c:/temp/malips.mp4"

    resync_audio_to_video(test_input_file, test_output_file)
