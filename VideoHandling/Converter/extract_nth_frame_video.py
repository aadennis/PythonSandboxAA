import os
import sys
import random
import subprocess
from pathlib import Path

def extract_nth_frame_video(source_folder, source_file, nth_frame=60):
    """
    Extracts every nth frame from a video file and rebuilds a new video using those frames.

    Args:
        source_folder (str): The folder containing the source video file.
        source_file (str): The name of the source video file.
        nth_frame (int): The interval for frame extraction (default is 60).
    """
    # Resolve paths for the source file and output file
    source_path = Path(source_folder) / source_file
    stem = Path(source_file).stem  # Get the filename without extension
    ext = Path(source_file).suffix  # Get the file extension
    rand_int = random.randint(1000, 9999)  # Generate a random integer for unique naming
    output_file = f"{stem}_{rand_int}{ext}"  # Create a unique output filename
    output_path = Path(source_folder) / output_file

    # Create a temporary folder to store extracted frames
    temp_dir = Path(source_folder) / f"frames_{rand_int}"
    temp_dir.mkdir(exist_ok=True)

    # Step 1: Extract every nth frame from the video
    extract_cmd = [
        "ffmpeg",  # Use ffmpeg for video processing
        "-i", str(source_path),  # Input video file
        "-vf", f"select='not(mod(n\\,{nth_frame}))',setpts=N/FRAME_RATE/TB",  # Select every nth frame
        "-vsync", "vfr",  # Variable frame rate to avoid duplicate frames
        str(temp_dir / "frame_%04d.png")  # Save frames as PNG images in the temp folder
    ]
    subprocess.run(extract_cmd, check=True)  # Run the ffmpeg command to extract frames

    # Step 2: Rebuild a new video from the extracted frames
    rebuild_cmd = [
        "ffmpeg",  # Use ffmpeg for video processing
        "-framerate", "30",  # Set the frame rate for the new video (default is 30 fps)
        "-i", str(temp_dir / "frame_%04d.png"),  # Input the extracted frames
        "-c:v", "libx264",  # Use the H.264 codec for video compression
        "-pix_fmt", "yuv420p",  # Set the pixel format for compatibility
        str(output_path)  # Output the rebuilt video
    ]
    subprocess.run(rebuild_cmd, check=True)  # Run the ffmpeg command to rebuild the video

    # Optional cleanup: Remove the temporary frames and directory
    for f in temp_dir.glob("*.png"):  # Delete all extracted frame images
        f.unlink()
    temp_dir.rmdir()  # Remove the temporary directory

    # Print the location of the output video
    print(f"✅ Output saved to: {output_path}")

# Entry point for the script
if __name__ == "__main__":
    # Check if the required arguments are provided
    if len(sys.argv) < 3:
        print("Usage:py extract_nth_frame_video.py <source_folder> <source_file> [nth_frame]")
        sys.exit(1)

    # Parse command-line arguments
    folder = sys.argv[1]  # Source folder
    file = sys.argv[2]  # Source file
    nth = int(sys.argv[3]) if len(sys.argv) > 3 else 60  # Frame interval (default is 60)

    # Call the function to process the video
    extract_nth_frame_video(folder, file, nth)

