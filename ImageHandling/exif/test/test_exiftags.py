"""
    Test module for exif tags
    pylint test_exiftags.py
    pytest-3 ./test_exiftags.py -v
"""
# https://docs.python.org/3/library/unittest.html
import shutil
from _pytest.outcomes import skip
import pytest
import os
from ImageHandling.exif.src.exiftags import ExifTags, ExifTagsList

def exiftool_exists():
    """
    Paired with skip_test_check, 
    naive check of whether exif tool is on the current environment.
    This is determined by the existence of EXIFTOOL=Y, which should
    only be true on a local environment, as exif tool should never be
    committed onto GitHub. Set this value using export EXIFTOOL=Y
    on the local server, never the GitHub server
    """

    try:
        os.environ['EXIFTOOL']
    except:
        return False
    return True

def skip_test_check():
    result = exiftool_exists()
    if not result:
        msg = "Exif tool not found. Test skipped"
        print(msg)
        pytest.skip(msg)
        


# pylint: disable=R0201
class TestExiftagsTestCase:
    """
        Test class exif tags
    """
    @pytest.fixture(scope="function", autouse=True)
    def set_up(self, tmp_path):
        """
            Setup fixture to run before each test method
        """
        for i in ["palette_no_tags.jpg", "tpaste.jpg"]:
            print(f"function-level test setup - tmp_path:\n {tmp_path}")
            target_file = tmp_path / i
            target_file2 = f"{tmp_path}/copy_{i}"
            shutil.copyfile(f"ImageHandling/exif/test/assets/image_files/{i}", target_file)
            shutil.copyfile(f"ImageHandling/exif/test/assets/image_files/{i}", target_file2)
    def test_file_not_exists(self):
        """
            Expect the requested file not to exist
        """
        with pytest.raises(FileNotFoundError):
            ExifTags("nonsense")

    def test_file_exists(self, tmp_path):
        """
            Expect the requested file to exist.
            info: tmp_path is a fixture of pytest. It does not exist under
            UnitTest or native Python.
        """
        exif_tags = ExifTags(tmp_path / "palette_no_tags.jpg")
        assert exif_tags is not None

    def test_get_tag_set_from_file(self, tmp_path):
        """
            The set of tags in a known file should match the expected format
        """
        skip_test_check()
        expected_response = " aaaaTattyRumPunches;other tags"
        exif_tags = ExifTags(tmp_path / "tpaste.jpg")
        response = exif_tags.get_tag_set()
        response = response.replace("\\r", "")
        assert expected_response == response

    def test_cannot_add_tags_if_additional_tags_is_N(self, tmp_path):
        """
            Expect failure when trying to add tags to a file which already has 1 or more tags,
            if not expliclity requested.
        """
        skip_test_check()
        exif_tags = ExifTags(tmp_path / "tpaste.jpg")
        with pytest.raises(AssertionError):
            exif_tags.set_tag_set("Should not succeed")

    def test_can_add_tags_if_additional_tags_is_Y(self, tmp_path):
        """
            Expect success when adding tags to a file which already has 1 or more tags,
            if expliclity requested.
        """
        skip_test_check()
        exif_tags = ExifTags(tmp_path / "tpaste.jpg")
        exif_tags.set_tag_set("Should succeed on Y", 'Y')
        print(f"this is it: {exif_tags.get_tag_set()}")

    def test_add_tags_if_no_existing_tagset(self, tmp_path):
        """
            Expect success when adding tags to a file which has zero tags
        """
        skip_test_check()
        expected_tag_set = " This set; should succeed"
        exif_tags = ExifTags(tmp_path / "palette_no_tags.jpg")
        exif_tags.set_tag_set("This set; should succeed")
        tag_set = exif_tags.get_tag_set()
        tag_set = tag_set.replace("\\r", "")
        assert expected_tag_set == tag_set

    def test_add_tags_if_existing_tagset(self, tmp_path):
        """
            Expect success when adding tags to a file which has zero tags
        """
        skip_test_check()
        expected_tag_set = "b'Subject                         : This set; should succeed\\n'"
        exif_tags = ExifTags(tmp_path / "tpaste.jpg")
        tag_set = exif_tags.get_tag_set()
        tag_set = tag_set.replace("\\r", "")
        print(f"returning.... {tag_set}")

    def test_add_same_tagset_to_all_jpgs_in_folder(self, tmp_path):
        """
            Add the same set of tags to all jpgs in the test folder.
            todo: this is just a syntax check - do a meaningful test.
        """
        skip_test_check()
        expected_tag_set = "Calvin Klein"
        tag_set = "trawler;fishing"
        append_ok = "Y"
        ExifTagsList(tmp_path, tag_set, append_ok)
        
        
