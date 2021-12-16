# pip install -U mock
# pip install pytest-mock # sic
import shutil
import pytest
from pytest_mock import mocker
from ImageHandling.exif.src.exiftags import ExifTags

#@pytest.fixture(autouse=True)

# pylint: disable=R0201
class TestitAll:
    @pytest.fixture(scope="function", autouse=True)
    def set_up(self, tmp_path):
        """
            Setup fixture to run before each test method
        """
        for i in ["palette_no_tags.jpg", "tpaste.jpg"]:
            print(f"function-level test setup - tmp_path:\n {tmp_path}")
            target_file = tmp_path / i
            shutil.copyfile(f"ImageHandling/exif/test/assets/image_files/{i}", target_file)

    @pytest.mark.skip("todo")
    def test_mock_get_tag_set(self, mocker, tmp_path):
        nt = ExifTags.NO_TAGS
        mocker.patch('ImageHandling.exif.src.exiftags.ExifTags.run_subprocess', return_value = nt)
        mocker.patch('ImageHandling.exif.src.exiftags.ExifTags.get_tag_set')
        exif_tags = ExifTags(tmp_path / "palette_no_tags.jpg")
        response = exif_tags.set_tag_set("alf")
        exif_tags.get_tag_set.assert_called_once()
        response = response.replace("\\r", "")
        expected_response = "asdfadf"
        assert expected_response == response
