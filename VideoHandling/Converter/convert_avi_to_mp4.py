import os
import subprocess
from datetime import datetime

# Set input/output folders
input_folder = "c:/temp/demo"  # Change to your folder path
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
        credits_text = f"{filename}\\nLast Modified: {file_date}"
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

        print(f"AAAAAA {credits_path}")
        credits_path = credits_path.replace("\\", "/")
        print(f"AAAAAA2 {credits_path}")

        # Replace backslashes with forward slashes for both paths
        credits_path = credits_path.replace("\\", "/")
        intermediate_path = intermediate_path.replace("\\", "/")

        # Write the paths directly to the concat list file
        with open(concat_list_path, "w") as f:
            f.write(f"file '{credits_path}'\n")
            f.write(f"file '{intermediate_path}'\n")


        concat_command = [
            ffmpeg_path, "-y",
            "-f", "concat", "-safe", "0",
            "-i", concat_list_path,
            "-c", "copy",
            final_path
        ]
        print(f"concat_list_path XXXXXXXXXXXXX: {concat_list_path}")
        print(f"credits_command XXXXXXXXXXXXX: {credits_command}")
        print(f"intermediate_path XXXXXXXXXXXXX: {intermediate_path}")
        print(f"concat_command XXXXXXXXXXXXX: {concat_command}")

        subprocess.run(concat_command, check=True)

        # Cleanup intermediate files
        os.remove(intermediate_path)
        os.remove(credits_path)
        os.remove(concat_list_path)

print("Batch conversion complete!")

