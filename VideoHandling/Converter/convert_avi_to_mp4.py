import os
import subprocess
from datetime import datetime

# Set the directory containing AVI files (or use the current directory)
input_folder = "c:/temp/demo"  # Change this to your actual folder path
output_folder = input_folder  # Change if you want output in a different folder

# Ensure FFmpeg is installed and accessible
ffmpeg_path = "ffmpeg"  # Adjust this if needed

# Process all .avi files in the folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".avi"):
        input_path = os.path.join(input_folder, filename)

        # Get last modified date of the file
        mod_time = os.path.getmtime(input_path)
        file_date = datetime.fromtimestamp(mod_time).strftime("%Y_%m_%d")

        # Construct output filename
        root_name, _ = os.path.splitext(filename)
        output_filename = f"{file_date}_{root_name}.mp4"
        output_path = os.path.join(output_folder, output_filename)

        # FFmpeg command for conversion
        command = [
            ffmpeg_path, "-i", input_path, "-vf", "bwdif",
            "-c:v", "h264_nvenc", "-c:a", "aac", "-b:a", "192k", output_path
        ]

        # Run the command
        print(f"Converting: {filename} -> {output_filename}")
        subprocess.run(command, check=True)

print("Batch conversion complete!")
