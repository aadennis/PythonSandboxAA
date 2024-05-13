from PIL import ExifTags, Image, ImageDraw, ImageFont

import os
import subprocess
from datetime import datetime

class Photo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.creation_date = None

    def get_creation_date(self):
        try:
            exif_data = subprocess.check_output(
                ['exiftool', '-CreateDate', '-d', '%Y-%m-%d %H:%M:%S', self.file_path]).decode('utf-8')
            creation_date_str = exif_data.split(': ')[1].strip()
            self.creation_date = datetime.strptime(
                creation_date_str, '%Y-%m-%d %H:%M:%S')
        except subprocess.CalledProcessError as e:
            print(f"Error while getting creation date for {
                  self.file_path}: {e}")
        except IndexError as e:
            print(f"Failed to extract creation date from EXIF data for {
                  self.file_path}: {e}")

    def set_text(self, text, font_size=36):
        font = ImageFont.load_default()
        font = font.font_variant(size=font_size)
        text_width = int((len(text) * font_size // 2) * 1.05)
        text_height = int(font_size * 1.3)
        text_image = Image.new(
            "RGB", (text_width + 10, text_height + 10), color="black")
        text_draw = ImageDraw.Draw(text_image)
        text_draw.text((5, 5), text, fill="white", font=font)

        return text_image

    def set_orientation(self, image):
        if hasattr(image, '_getexif'):  # only present in JPEGs
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            e = image._getexif()
            if e is not None:
                exif = dict(e.items())

                if orientation in exif:
                    if exif[orientation] == 3:
                        image = image.rotate(180, expand=True)
                    elif exif[orientation] == 6:
                        image = image.rotate(270, expand=True)
                    elif exif[orientation] == 8:
                        image = image.rotate(90, expand=True)
        return image

    def write_on_image(self, text, name_modifier, font_size=36):
        image = Image.open(self.file_path)
        image = self.set_orientation(image)
        text_image = self.set_text(text, font_size)
        image.paste(text_image, (10, 10))
        output_path = f"{os.path.splitext(self.file_path)[0]}_{
            name_modifier}.jpg"
        image.save(output_path)
        return output_path
