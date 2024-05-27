import os
import shutil
from Photo import Photo

# todo - png support for dates

class ImageHandler:
    def __init__(self, source_dir, destination_dir):
        self.source_dir = source_dir
        self.destination_dir = destination_dir
        self.photos_added_counts = {}

    def process_images(self):
        for file_name in os.listdir(self.source_dir):
            print(f"Now on [{file_name}] in [{self.source_dir}]")
            file_path = os.path.join(self.source_dir, file_name)

            if file_name.lower().endswith(('.jpeg', '.jpg')):
                try:
                    image_obj = Photo(file_path)
                    image_obj.get_creation_date()

                    if image_obj.creation_date:
                        creation_date_str = image_obj.creation_date.strftime('%Y-%m-%d')
                        modified_image_path = image_obj.write_on_image(creation_date_str, name_modifier="ANYTHING_BUT", font_size=72)

                        year_folder = image_obj.creation_date.strftime('%Y')
                        month_folder = image_obj.creation_date.strftime('%Y-%m')
                        destination_folder = os.path.join(self.destination_dir, year_folder, month_folder)

                        os.makedirs(destination_folder, exist_ok=True)

                        shutil.copy2(modified_image_path, destination_folder)

                        self.photos_added_counts[destination_folder] = self.photos_added_counts.get(destination_folder, 0) + 1

                        os.remove(modified_image_path)
                except Exception as e:
                    print(f"Failed to process image {file_path}: {e}")

        print("Counts of photos added to each folder:")
        for folder, count in self.photos_added_counts.items():
            print(f"{folder}: {count} photos")

        print("Photo files have been copied to the appropriate folders.")
