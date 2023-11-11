"""
    Read a video file, writing the audio track to its own file.
"""

from moviepy.video.io.VideoFileClip import VideoFileClip


def get_audio_from_video(input_file, output_file):
    """
    Read a video file, writing the audio track to its own file.
    """
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)

def main():
    """
    wrapper to the single function
    """
    input_file = r"c:\temp\Artrage Lock Transparency V1.mp4"
    output_file = r"c:\temp\mahaudioxx.mp3"
    get_audio_from_video(input_file, output_file)

if __name__ == "__main__":
    main()

