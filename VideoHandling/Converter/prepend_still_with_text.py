import subprocess
import sys

def extract_frame(input_video, frame_image):
    """Extracts a single frame from the video at 1 second."""
    subprocess.run([
        "ffmpeg", "-y",
        "-i", input_video,
        "-ss", "00:00:01",  # Extract frame at 1 second to avoid black frames
        "-frames:v", "1",
        frame_image
    ], check=True)

def add_text_to_frame(frame_image, output_image):
    """Adds 'test' text to the extracted frame."""
    subprocess.run([
        "ffmpeg", "-y",
        "-i", frame_image,
        "-vf", "drawtext=text='test':fontcolor=white:fontsize=60:x=(w-text_w)/2:y=(h-text_h)/2",
        output_image
    ], check=True)

def create_intro_video(frame_image, output_video, duration, input_video):
    """Converts the image to a short video with the same properties as the input video."""
    subprocess.run([
        "ffmpeg", "-y",
        "-loop", "1",  # Loop single image
        "-i", frame_image,
        "-t", str(duration),  # Duration in seconds
        "-i", input_video,  # Reference for matching framerate
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-vf", "fps=fps=25,format=yuv420p",  # Ensure compatibility
        output_video
    ], check=True)

def concatenate_videos(intro_video, input_video, output_video):
    """Concatenates the intro video with the original video while keeping audio."""
    with open("file_list.txt", "w") as f:
        f.write(f"file '{intro_video}'\n")
        f.write(f"file '{input_video}'\n")

    subprocess.run([
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", "file_list.txt",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        output_video
    ], check=True)

def prepend_frame_to_video(input_video, output_video, duration=2):
    """Runs the full pipeline to prepend a frame with text to a video."""
    frame_image = "frame.jpg"
    text_frame_image = "frame_text.jpg"
    intro_video = "intro.mp4"

    extract_frame(input_video, frame_image)
    add_text_to_frame(frame_image, text_frame_image)
    create_intro_video(text_frame_image, intro_video, duration, input_video)
    concatenate_videos(intro_video, input_video, output_video)

    # Cleanup
    subprocess.run(["rm", frame_image, text_frame_image, intro_video, "file_list.txt"], check=True)

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Usage: python script.py input.mp4 output.mp4")
    #     sys.exit(1)

    input_video = 'input.mp4'
    output_video = 'output.mp4'
    
    prepend_frame_to_video(input_video, output_video)


