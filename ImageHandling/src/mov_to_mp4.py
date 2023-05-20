# https://python-ffmpeg.readthedocs.io/en/latest/
# pip install python-ffmpeg

from ffmpeg import FFmpeg

input_file = "c:/temp/a.mov"
output_file = "c:/temp/a.mp4"

def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input(input_file)
        .output(
            output_file,
            {"codec:v": "libx264"},
            vf="scale=1280:-1",
            preset="veryslow",
            crf=24,
        )
    )

    ffmpeg.execute()

if __name__ == "__main__":
    main()