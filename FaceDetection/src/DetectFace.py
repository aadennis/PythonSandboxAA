import cv2
import os
import shutil

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Specify the source folder and target folder
src_folder = 'c:/temp/test_images'
target_folder = 'c:/temp/outfaces'

# Iterate through all images in the source folder
for filename in os.listdir(src_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Read the image
        img = cv2.imread(os.path.join(src_folder, filename))
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # If a face is detected, move the image to the target folder
        if len(faces) > 0:
            shutil.move(os.path.join(src_folder, filename), target_folder)
