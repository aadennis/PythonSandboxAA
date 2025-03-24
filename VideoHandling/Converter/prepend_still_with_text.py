# Prepend a still image with some fixed text to the beginning of an existing MP4 video.
# Ensure that the video retains its original audio after the modification.
# The final output should have the prepended still image shown for a few seconds before continuing with the original video.
# Maintain video and audio synchronization, so there are no changes to the original audio track, and the video doesn’t 
# get unintentionally truncated.
# https://chatgpt.com/share/67e1cbad-6414-8011-9d5f-1d376ed05b56

import subprocess
import os
import sys

def extract_first_frame(input_video, output_image, text="test"):
    """Extracts the first frame of the video to an image with text."""
    subprocess.run([
        "ffmpeg", "-i", input_video, "-vf", f"select='eq(n\\,0)',drawtext=text='{text}':x=(w-text_w)/2:y=(h-text_h)/2:fontcolor=white:fontsize=50",
        "-vsync", "vfr", "-q:v", "2", output_image
    ], check=True)

def create_still_video(input_image, output_video, duration):
    """Creates a silent video from the still image."""
    subprocess.run([
        "ffmpeg", "-loop", "1", "-framerate", "2", "-t", str(duration),
        "-i", input_image, "-f", "lavfi", "-t", str(duration), 
        "-i", "anullsrc=r=44100:cl=stereo", "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-strict", "experimental", output_video
    ], check=True)

def extract_audio_segment(input_video, output_audio, duration):
    """Extracts the audio from the video for the desired duration."""
    subprocess.run([
        "ffmpeg", "-i", input_video, "-t", str(duration), "-vn", "-acodec", "aac", output_audio
    ], check=True)

def merge_still_with_audio(silent_video, audio_segment, output_video):
    """Merges the silent video with the audio segment, preserving original audio characteristics."""
    subprocess.run([
        "ffmpeg", "-i", silent_video, "-i", audio_segment, "-c:v", "libx264", "-c:a", "aac",
        "-strict", "experimental", "-shortest", "-map", "0:v:0", "-map", "1:a:0", output_video
    ], check=True)

def concatenate_videos(intro_video, input_video, output_video):
    """Concatenates the intro video and original video into the output."""
    with open("file_list.txt", "w") as f:
        f.write(f"file '{intro_video}'\n")
        f.write(f"file '{input_video}'\n")
    
    subprocess.run([
        "ffmpeg", "-f", "concat", "-safe", "0", "-i", "file_list.txt", "-c", "copy", output_video
    ], check=True)



def prepend_frame_to_video(input_video, output_video, duration=2):
    """Runs the full pipeline to prepend a still frame with audio to a video."""
    frame_image = "frame_text.jpg"
    silent_video = "silent.mp4"
    audio_segment = "audio_segment.aac"
    intro_video = "intro.mp4"

    # Extract first frame with text
    extract_first_frame(input_video, frame_image)

    
    # Create the silent video (2 seconds of intro with extracted frame)
    create_still_video(frame_image, silent_video, duration)

    # Extract audio segment for the intro duration
    extract_audio_segment(input_video, audio_segment, duration)

    # Merge the silent video with audio
    merge_still_with_audio(silent_video, audio_segment, intro_video)

    # Concatenate the intro and the original video
    concatenate_videos(intro_video, input_video, output_video)

    # Cleanup files after processing
    for file in [silent_video, audio_segment, intro_video, frame_image, "file_list.txt"]:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass  # Ignore missing files

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Usage: python script.py input.mp4 output.mp4")
    #     sys.exit(1)

    input_video = 'input.mp4'
    output_video = 'output.mp4'

    prepend_frame_to_video(input_video, output_video)

