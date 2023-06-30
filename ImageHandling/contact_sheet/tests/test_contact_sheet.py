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
        max_images = 200

        # act
        contact_sheet = ContactSheet(img_folder, max_images= max_images, column_count = 6)
