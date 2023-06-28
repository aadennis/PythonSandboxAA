from src.contact_sheet import make_contact_sheet

class TestContactSheet(object): 
    img_folder = "tests/TestImageFiles"
       
    def test_small_volume_set1(self):
        # arrange
        output_file = "c:/temp/smallstuff.jpg"
        # act
        contact_sheet = make_contact_sheet(self.img_folder, output_file)

    def test_large_volume_set1(self):
        # arrange
        # override test class default
        img_folder = "D:/onedrive/data/photos/_Albums/CameraRollDump/CRD_2023_01"
        output_file = "c:/temp/stuff.jpg"
        max_images = 100

        # act
        contact_sheet = make_contact_sheet(img_folder, output_file, max_images= max_images, column_count = 3)
