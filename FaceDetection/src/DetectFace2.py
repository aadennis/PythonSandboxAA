import dlib
import os
import shutil
import numpy as np
from PIL import Image

class FaceDetector:
    def __init__(self, src_folder, target_face_folder, target_notface_folder):
        self.detector = dlib.get_frontal_face_detector()
        self.src_folder = src_folder
        self.target_face_folder = target_face_folder
        self.target_notface_folder = target_notface_folder
        

    def detect_faces(self):
        for filename in os.listdir(self.src_folder):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                img = Image.open(os.path.join(self.src_folder, filename))
                gray = img.convert('L')
                gray = np.array(gray)
                faces = self.detector(gray, 1)
                if len(faces) > 0:
                    print("got a face: " + filename)
                    shutil.copyfile(os.path.join(self.src_folder, filename), os.path.join(self.target_face_folder, filename))
                else:
                    print("NOT a face: " + filename)
                    shutil.copyfile(os.path.join(self.src_folder, filename), os.path.join(self.target_notface_folder, filename))
            


# Usage
# src_image_folder = 'FaceDetection/test/test_images/medium'
#     fd = FaceDetector(src_image_folder, target_face_folder, target_notface_folder)
#     fd.detect_faces()
#     for dir in (target_face_folder, target_notface_folder):
#         with os.scandir(dir) as it:
#             for entry in it:
#                 print(entry.name, entry.path)
