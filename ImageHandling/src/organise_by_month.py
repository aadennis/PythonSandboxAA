import os
import subprocess
import shutil
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

class ImageObject:
    def __init__(self, file_path):
        self.file_path = file_path
        self.creation_date = None

    def get_creation_date(self):
        try:
            exif_data = subprocess.check_output(['exiftool', '-CreateDate', '-d', '%Y-%m-%d %H:%M:%S', self.file_path]).decode('utf-8')
            creation_date_str = exif_data.split(': ')[1].strip()
            self.creation_date = datetime.strptime(creation_date_str, '%Y-%m-%d %H:%M:%S')
        except subprocess.CalledProcessError as e:
            print(f"Error while getting creation date for {self.file_path}: {e}")
        except IndexError as e:
            print(f"Failed to extract creation date from EXIF data for {self.file_path}: {e}")

class ImageHandler:
    def __init__(self, source_dir, destination_dir):
        self.source_dir = source_dir
        self.destination_dir = destination_dir
        self.photos_added_counts = {}

    def write_on_image(self, image_obj, text, name_modifier, font_size=36):
        image = Image.open(image_obj.file_path)

        font = ImageFont.load_default()
        font = font.font_variant(size=font_size)

        text_width = int((len(text) * font_size // 2) * 1.05)
        text_height = int(font_size * 1.3)
        
        text_image = Image.new("RGB", (text_width + 10, text_height + 10), color="black")
        text_draw = ImageDraw.Draw(text_image)
        text_draw.text((5, 5), text, fill="white", font=font)

        image.paste(text_image, (10, 10))

        output_path = f"{os.path.splitext(image_obj.file_path)[0]}_{name_modifier}.jpg"
        image.save(output_path)
        return output_path

    def process_images(self):
        for file_name in os.listdir(self.source_dir):
            print(f"Now on [{file_name}] in [{self.source_dir}]")
            file_path = os.path.join(self.source_dir, file_name)

            if file_name.lower().endswith(('.jpeg', '.jpg')):
                try:
                    image_obj = ImageObject(file_path)
                    image_obj.get_creation_date()

                    if image_obj.creation_date:
                        creation_date_str = image_obj.creation_date.strftime('%Y-%m-%d')
                        modified_image_path = self.write_on_image(image_obj, creation_date_str, name_modifier="ANYTHING_BUT", font_size=72)
                        
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

# Usage
source_dir = 'ImageHandling/tests/TestImageFiles/'
destination_dir = 'TestOutput'
handler = ImageHandler(source_dir, destination_dir)
handler.process_images()