import subprocess
import os
import random
import argparse

def get_video_duration(input_file):
    """Returns duration in seconds using ffprobe, with error handling."""
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', input_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    raw_output = result.stdout.strip()
    if not raw_output:
        raise ValueError(f"❌ ffprobe failed. stderr: {result.stderr.strip()}")
    return float(raw_output)

def split_video(input_file, split_count=2):
    duration = get_video_duration(input_file)
    segment_duration = duration / split_count
    base_name, ext = os.path.splitext(input_file)
    rand_id = random.randint(1000, 9999)

    for i in range(split_count):
        start_time = i * segment_duration
        output_file = f"{base_name}_{rand_id}_{i+1}.mp4"
        print(f"🔧 Creating segment {i+1}/{split_count}: {output_file}")

        subprocess.run([
            'ffmpeg', '-y', '-ss', str(start_time), '-i', input_file,
            '-t', str(segment_duration), '-c', 'copy', output_file
        ])

    print(f"✅ Done. Created {split_count} segments with ID {rand_id}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split MP4 into equal parts.")
    parser.add_argument("input_file", help="Path to input MP4 file")
    parser.add_argument("--split_count", type=int, default=2, help="Number of segments (default: 2)")
    args = parser.parse_args()

    split_video(args.input_file, args.split_count)

 