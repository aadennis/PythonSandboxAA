"""
    Create a copy of an mp4 file, but saving only 1 in every n frames.

    Documentation:
    ----------------
    This script processes an input video file and creates a new video by saving only 
    every nth frame. It uses the `opencv-python` library for video processing.

    Dependencies:
    --------------
    - Python 3.x
    - OpenCV library: Install it using `pip install opencv-python`.

    Key Variables:
    ---------------
    - INPUT_FILE: Path to the input video file.
    - OUTPUT_FILE: Path to the output video file.
    - FRAME_INTERVAL: Interval for selecting frames (e.g., 10 means every 10th frame).

    Functions:
    -----------
    extract_frames(input_file, output_file, frame_interval):
        - Reads the input video file.
        - Extracts every nth frame based on the `frame_interval`.
        - Writes the selected frames to a new video file.
        - Parameters:
            - input_file: Path to the input video file.
            - output_file: Path to the output video file.
            - frame_interval: Interval for selecting frames.

    How to Run:
    ------------
    1. Ensure the `opencv-python` library is installed.
    2. Set the `INPUT_FILE` variable to the path of your input video file.
    3. Set the `OUTPUT_FILE` variable to the desired path for the output video file.
    4. Set the `FRAME_INTERVAL` variable to the desired frame interval (e.g., 10 for every 10th frame).
    5. Run the script:
       python shrink_movie.py
    6. The output video will be saved to the path specified in `OUTPUT_FILE`.

    Notes:
    -------
    - Ensure the input file path is correct and accessible.
    - The output file path must be writable.
    - Adjust the `FRAME_INTERVAL` variable to control how many frames are skipped.
    - The script assumes the input video is in `.mp4` format and uses the `mp4v` codec for the output
"""

import cv2

INPUT_FILE = 'c:/tempx/sidmouth.mp4'  # Replace with your input file name
OUTPUT_FILE = 'c:/tempx/sidm_short.mp4'  # Replace with your output file name
FRAME_INTERVAL = 10

def extract_frames(input_file, output_file, frame_interval):
    cap = cv2.VideoCapture(input_file)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            out.write(frame)

        frame_count += 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()



extract_frames(INPUT_FILE, OUTPUT_FILE, FRAME_INTERVAL)
print("New video created with every 10th frame!")
