import pytest
import tempfile
import os
from pathlib import Path 
from collections import Counter

from ..src.DetectFace2 import FaceDetector

# Test the FaceDetector class.
# Check that the images with faces, and without faces, are moved into 
# their respective triage folders.
# "Real" source folders are used for the original images (small-ish pics).
# For the triage target folders, the Python tempfile library is used,
# because a) using concrete target folders can result in locking and/
# or permission issues, and b) for ease of teardown... there is none.
# A fixture using with/yield ensures that the tempdir dir remains in
# scope for each test, and for some separation of setup and test.

class TestImageMove:
    @pytest.fixture(autouse=True)
    def temp_dir(self):
        with tempfile.TemporaryDirectory() as tempdir:
            self.tempdir = tempdir
            self.target_face_folder = os.path.join(self.tempdir, 'faces')
            self.target_notface_folder = os.path.join(self.tempdir, 'notfaces')
            os.mkdir(self.target_face_folder)
            os.mkdir(self.target_notface_folder)
            yield

    def test_images_are_triaged_ok(self):
        file_path = Path(__file__).absolute()
        dir_path =  Path().absolute()

        fd = FaceDetector("FaceDetection/test/test_images/medium", self.target_face_folder, self.target_notface_folder)
        expected_face_array = ["FullLassie.png","bloke.png","MaLassie.png"]
        expected_notface_array = ["APorthole.png","bike.png","pizza01x.jpg"]
        fd.detect_faces()
        actual_face_array = []
        for dir in (self.target_face_folder,):
            with os.scandir(dir) as it:
                for entry in it:
                    actual_face_array.append(entry.name)
        actual_notface_array = []
        for dir in (self.target_notface_folder,):
            with os.scandir(dir) as it:
                for entry in it:
                    actual_notface_array.append(entry.name)

        assert Counter(expected_face_array) == Counter(actual_face_array)
        assert Counter(expected_notface_array) == Counter(actual_notface_array)
        
# usage
# pytest .\FaceDetection -vv -s