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
    input_dir = r"c:\temp"
    input_file = r"\Artrage Lock Transparency V1"
    input_file_with_ext = input_dir + input_file + ".mp4"
    output_file_with_ext = input_dir + input_file + ".mp3"
    
    get_audio_from_video(input_file_with_ext, output_file_with_ext)

if __name__ == "__main__":
    main()

