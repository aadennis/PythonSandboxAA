import dlib
import os
import shutil
import numpy as np
from PIL import Image

# Load the detector
detector = dlib.get_frontal_face_detector()

# Specify the source folder and target folder
src_folder = 'c:/temp/test_images'
target_folder = 'c:/temp/outfaces'

# Iterate through all images in the source folder
for filename in os.listdir(src_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Read the image
        img = Image.open(os.path.join(src_folder, filename))
        # Convert the image into grayscale
        gray = img.convert('L')
        # Convert the PIL Image to a numpy array
        gray = np.array(gray)
        # Detect faces
        faces = detector(gray, 1)
        # If a face is detected, move the image to the target folder
        if len(faces) > 0:
            print("got a face: " + filename)
            shutil.move(os.path.join(src_folder, filename), target_folder)
        else:
            print("NOT a face: " + filename)
