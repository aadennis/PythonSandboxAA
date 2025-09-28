import subprocess
import sys
import random
import os

def get_video_duration(input_file):
    """Returns duration in seconds using ffprobe, with error handling."""
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
         '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',
         input_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    raw_output = result.stdout.strip()
    if not raw_output:
        print(f"❌ ffprobe failed or returned no duration.")
        print(f"stderr: {result.stderr.strip()}")
        raise ValueError("Could not retrieve video duration. Check input file and ffprobe availability.")

    try:
        return float(raw_output)
    except ValueError:
        print(f"❌ Failed to parse duration from ffprobe output: '{raw_output}'")
        raise

def generate_output_filename(input_file):
    """Generates output filename: inputname_randomint.mp4"""
    base, ext = os.path.splitext(input_file)
    rand_int = random.randint(1000, 9999)
    return f"{base}_{rand_int}.mp4"

def extract_portion(input_file, percentage_along, portion_as_percentage):
    duration = get_video_duration(input_file)
    start_time = (percentage_along / 100.0) * duration
    clip_duration = (portion_as_percentage / 100.0) * duration

    if start_time + clip_duration > duration:
        clip_duration = duration - start_time
        print(f"⚠️ Warning: Requested portion exceeds video length. Clipping to end.")

    output_file = generate_output_filename(input_file)

    subprocess.run([
        'ffmpeg', '-y', '-ss', str(start_time), '-i', input_file,
        '-t', str(clip_duration), '-c', 'copy', output_file
    ])

    print(f"✅ Saved clip as: {output_file}")

# Example usage
if __name__ == "__main__":
    input_mp4 = "c:/temp/downloads/norm0005.mp4"
    percentage_along = 0
    portion_as_percentage = 99
    extract_portion(input_mp4, percentage_along, portion_as_percentage)

    