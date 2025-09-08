import os
import sys
import random
import subprocess
from pathlib import Path

def extract_nth_frame_video(source_folder, source_file, nth_frame=60):
    # Resolve paths
    source_path = Path(source_folder) / source_file
    stem = Path(source_file).stem
    ext = Path(source_file).suffix
    rand_int = random.randint(1000, 9999)
    output_file = f"{stem}_{rand_int}{ext}"
    output_path = Path(source_folder) / output_file

    # Create temp folder for frames
    temp_dir = Path(source_folder) / f"frames_{rand_int}"
    temp_dir.mkdir(exist_ok=True)

    # Step 1: Extract every nth frame
    extract_cmd = [
        "ffmpeg",
        "-i", str(source_path),
        "-vf", f"select='not(mod(n\\,{nth_frame}))',setpts=N/FRAME_RATE/TB",
        "-vsync", "vfr",
        str(temp_dir / "frame_%04d.png")
    ]
    subprocess.run(extract_cmd, check=True)

    # Step 2: Rebuild video from extracted frames
    rebuild_cmd = [
        "ffmpeg",
        "-framerate", "30",  # You can tweak this if needed
        "-i", str(temp_dir / "frame_%04d.png"),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        str(output_path)
    ]
    subprocess.run(rebuild_cmd, check=True)

    # Optional cleanup
    for f in temp_dir.glob("*.png"):
        f.unlink()
    temp_dir.rmdir()

    print(f"✅ Output saved to: {output_path}")

# Entry point
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:py extract_nth_frame_video.py <source_folder> <source_file> [nth_frame]")
        sys.exit(1)

    folder = sys.argv[1]
    file = sys.argv[2]
    nth = int(sys.argv[3]) if len(sys.argv) > 3 else 60

    extract_nth_frame_video(folder, file, nth)

