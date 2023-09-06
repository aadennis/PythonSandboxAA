"""
    Create a copy of an mp4 file, but saving only 1
    in every n frames.
"""
# pip install opencv-python

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
