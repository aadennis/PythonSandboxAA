import subprocess
import sys

def prepend_still_with_text(input_file, output_file):
    # Get input video details (resolution and framerate)
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height,r_frame_rate",
         "-of", "csv=p=0", input_file],
        capture_output=True, text=True, check=True
    )
    
    width, height, frame_rate = probe.stdout.strip().split(",")
    
    # Generate a 2-second still frame with text matching the input video resolution
    temp_still = "temp_still.mp4"
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", f"color=c=black:s={width}x{height}:d=2",
        "-vf", f"drawtext=text='test':fontcolor=white:fontsize=60:x=(w-text_w)/2:y=(h-text_h)/2",
        "-r", frame_rate,
        "-c:v", "libx264", "-t", "2", temp_still
    ], check=True)

    # Concatenate the still frame with the input video while keeping audio
    subprocess.run([
        "ffmpeg", "-y",
        "-i", temp_still, "-i", input_file,
        "-filter_complex", "[0:v:0][1:v:0]concat=n=2:v=1:a=0[outv];[1:a:0]adelay=2000|2000[outa]",
        "-map", "[outv]", "-map", "[outa]",
        "-c:v", "libx264", "-c:a", "aac", "-b:a", "192k", output_file
    ], check=True)

    # Clean up temp file
    subprocess.run(["rm", temp_still], check=True)

if __name__ == "__main__":

    input_video = 'input.mp4'
    output_video = './output.mp4'
    
    prepend_still_with_text(input_video, output_video)
