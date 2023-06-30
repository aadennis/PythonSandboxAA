from src.contact_sheet import ContactSheet

class TestContactSheet(object): 
    img_folder = "tests/TestImageFiles"
       
    def test_small_volume_set1(self):
        # act
        contact_sheet = ContactSheet(self.img_folder)

    def test_large_volume_set1(self):
        # arrange
        # override test class default
        img_folder = "D:/onedrive/data/photos/_Albums/CameraRollDump/CRD_2023_01"

        # edge cases to try:
        # max_images is exact multiple of rows * columns - is last page blank?
        # max_images is 1 less, then 1 more than a multiple of rows * columns
        # act
        contact_sheet = ContactSheet(img_folder, max_images= 240, requested_rows_per_page=10, column_count = 6)
