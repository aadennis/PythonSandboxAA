# pip install -U mock
# pip install pytest-mock # sic
import shutil
import pytest
from Utilities.src.utility import Utility
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

    def test_mock_get_tag_set(self, mocker, tmp_path):
        # arrange
        expected_response = "response from exif tool"
        mocker.patch('Utilities.src.utility.Utility.run_subprocess', return_value = expected_response)
        exif_tags = ExifTags(tmp_path / "palette_no_tags.jpg")
        # act
        response = exif_tags.get_tag_set()
        response = response.replace("\\r", "")
        
        # assert
        Utility().run_subprocess.assert_called_once()
        assert expected_response == response
