# Description: This script converts AVI files to MP4 files, deinterlacing the video and adding a 
# credit screen with the filename and last modified date.
# 
# Usage: Place this script in a folder with AVI files, and run it. 
# The script will convert all AVI files in the folder to MP4 files.
# The output MP4 files will have the same resolution as the original AVI files. Attempting a different
# resolution may result in interlace artifacts.

# Ensure FFmpeg and FFprobe are installed and in the system PATH. https://ffmpeg.org/download.html
# FFprobe is required to get the video resolution. 
# The script uses the NVIDIA NVENC hardware encoder for video conversion. Ensure the NVIDIA GPU drivers are installed.
# The script creates an intermediate MP4 file with deinterlacing and then concatenates it with a credit screen.
# The credit screen includes the filename and last modified date of the original AVI file.
# The final MP4 file is saved in the same folder as the original AVI file.
# The script cleans up intermediate files after conversion.
# The script uses the system date format (YYYY_MM_DD) for the credit screen.
# todo: The script uses the filename of the AVI file for the credit screen and for the final MP4 file
# https://chatgpt.com/share/67e09cf8-7a30-8011-97e1-a30006abfbaa

import os
import subprocess
from datetime import datetime

# Set input/output folders
input_folder = "test_data"  # Change to your folder path
output_folder = input_folder  # Change if needed

ffmpeg_path = "ffmpeg"

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".avi"):
        input_path = f"{input_folder}/{filename}"

        # Get last modified date
        mod_time = os.path.getmtime(input_path)
        file_date = datetime.fromtimestamp(mod_time).strftime("%Y_%m_%d")

        # Construct filenames
        root_name, _ = os.path.splitext(filename)
        intermediate_filename = f"{file_date}_{root_name}_intermediate.mp4"
        final_filename = f"{file_date}_{root_name}.mp4"

        intermediate_path = f"{output_folder}/{intermediate_filename}"
        final_path = f"{output_folder}/{final_filename}"

        # First pass: Convert the AVI to an intermediate MP4, preserving resolution
        convert_command = [
            ffmpeg_path, "-y",
            "-i", input_path,
            "-vf", "bwdif",  # Deinterlace
            "-c:v", "h264_nvenc",
            "-c:a", "aac", "-b:a", "192k",
            intermediate_path
        ]
        
        # convert_command = [
        #     ffmpeg_path, "-y",
        #     "-i", input_path,
        #     "-vf", "bwdif",  # Deinterlace video
        #     "-c:v", "h264_nvenc",  # Video codec (NVIDIA hardware encoding)
        #     "-c:a", "aac", "-b:a", "192k",  # Re-encode both audio streams to AAC
        #     "-map", "0:v:0",  # Map video stream
        #     "-map", "0:a:0",  # Map first audio stream
        #     "-map", "0:a:1?",  # Map second audio stream
        #     intermediate_path
        # ]



        subprocess.run(convert_command, check=True)

        # Use FFprobe to get the video resolution
        ffprobe_path = "ffprobe"  # Ensure FFprobe is in your system PATH
        resolution_cmd = [
            ffprobe_path, "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=width,height",
            "-of", "csv=p=0",
            intermediate_path
        ]

        resolution_output = subprocess.run(resolution_cmd, capture_output=True, text=True, check=True)
        width, height = resolution_output.stdout.strip().split(",")

        # Generate credit screen
        credits_text = f"{filename}\nLast Modified: {file_date}"
        credits_path = f"{output_folder}/credits.mp4"
        credits_command = [
            ffmpeg_path, "-y",
            "-f", "lavfi", "-i", f"color=s={width}x{height}:d=2:c=black",
            "-vf", f"drawtext=text='{credits_text}':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2",
            "-c:v", "libx264", "-t", "2",
            credits_path
        ]

        subprocess.run(credits_command, check=True)

        # Concatenate credits and intermediate file
        concat_list_path = f"{output_folder}/concat_list.txt"

        # Ensure paths are using forward slashes
        credits_path = credits_path.replace("\\", "/")
        intermediate_path = intermediate_path.replace("\\", "/")

        # Write relative paths for ffmpeg (no drive letter issue)
        with open(concat_list_path, "w") as f:
            f.write(f"file 'credits.mp4'\n")
            f.write(f"file '{intermediate_filename}'\n")

        concat_command = [
            ffmpeg_path, "-y",
            "-f", "concat", "-safe", "0",
            "-i", concat_list_path,
            "-c", "copy",
            final_path
        ]

        subprocess.run(concat_command, check=True)

        # Cleanup intermediate files
        # os.remove(intermediate_path)
        # os.remove(credits_path)
        # os.remove(concat_list_path)

print("Batch conversion complete!")

