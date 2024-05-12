import os
import subprocess
import shutil
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path 

class ImageHandler:
    def __init__(self, source_dir, destination_dir):
        self.source_dir = source_dir
        self.destination_dir = destination_dir
        self.photos_added_counts = {}

    def get_creation_date(self, file_path):
        try:
            exif_data = subprocess.check_output(['exiftool', '-CreateDate', '-d', '%Y-%m-%d %H:%M:%S', file_path]).decode('utf-8')
            creation_date_str = exif_data.split(': ')[1].strip()
            return datetime.strptime(creation_date_str, '%Y-%m-%d %H:%M:%S')
        except subprocess.CalledProcessError as e:
            print(f"Error while getting creation date for {file_path}: {e}")
            return None
        except IndexError as e:
            print(f"Failed to extract creation date from EXIF data for {file_path}: {e}")
            return None

    def write_on_image(self, image_path, text, name_modifier, font_size=36):
        # Preserve the original orientation of the image
        self.preserve_orientation(image_path, "temp_original.jpg")
        
        # Open the image from the temporary file with preserved orientation
        image = Image.open("temp_original.jpg")
        
        font = ImageFont.load_default()
        font = font.font_variant(size=font_size)

        text_width = int((len(text) * font_size // 2) * 1.05)
        text_height = int(font_size * 1.3)
        
        text_image = Image.new("RGB", (text_width + 10, text_height + 10), color="black")
        text_draw = ImageDraw.Draw(text_image)
        text_draw.text((5, 5), text, fill="white", font=font)

        image.paste(text_image, (10, 10))

        output_path = f"{os.path.splitext(image_path)[0]}_{name_modifier}.jpg"
        image.save(output_path)

        # Clean up temporary files
        os.remove("temp_original.jpg")

        return output_path
    
    def preserve_orientation(self, input_file, output_file):
        try:
            exif_data = subprocess.check_output(['exiftool', '-CreateDate', '-d', '%Y-%m-%d %H:%M:%S', input_file]).decode('utf-8')
            creation_date_str = exif_data.split(': ')[1].strip()
            creation_date = datetime.strptime(creation_date_str, '%Y-%m-%d %H:%M:%S')
            orientation = subprocess.check_output(['exiftool', '-Orientation', input_file]).decode('utf-8')
            orientation = orientation.split(': ')[1].strip()
            if orientation != 'Horizontal (normal)':
                Image.open(input_file).transpose(Image.ROTATE_270 if orientation == 'Rotate 270 CW' else Image.ROTATE_90).save(output_file)
            else:
                shutil.copy2(input_file, output_file)
        except subprocess.CalledProcessError as e:
            print(f"Error while getting orientation for {input_file}: {e}")
        except Exception as e:
            print(f"Failed to preserve orientation for {input_file}: {e}")



    def process_images(self):

        for file_name in os.listdir(self.source_dir):
            print(f"Now on [{file_name}] in [{self.source_dir}]")
            file_path = os.path.join(self.source_dir, file_name)

            if file_name.lower().endswith(('.jpeg', '.jpg')):
                try:
                    creation_date = self.get_creation_date(file_path)
                    print(creation_date)
                    temp_name="ANYTHING_BUT"
                    
                    creation_date_str = creation_date.strftime('%Y-%m-%d')
                    modified_image_path = self.write_on_image(file_path, creation_date_str, name_modifier=temp_name, font_size=72)
                    
                    year_folder = creation_date.strftime('%Y')
                    month_folder = creation_date.strftime('%Y-%m')
                    destination_folder = os.path.join(self.destination_dir, year_folder, month_folder)
                    
                    os.makedirs(destination_folder, exist_ok=True)
                    
                    shutil.copy2(modified_image_path, destination_folder)
                    
                    self.photos_added_counts[destination_folder] = self.photos_added_counts.get(destination_folder, 0) + 1
                    
                    os.remove(modified_image_path)
                except Exception as e:
                    print(f"Failed to get creation date for {file_path}: {e}")

        print("Counts of photos added to each folder:")
        for folder, count in self.photos_added_counts.items():
            print(f"{folder}: {count} photos")

        print("Photo files have been copied to the appropriate folders.")

# Usage
source_dir = 'ImageHandling/tests/TestImageFiles/'
destination_dir = 'd:/Sandbox/git/aadennis/PythonSandboxAA/TestOutput'
destination_dir = 'TestOutput'
handler = ImageHandler(source_dir, destination_dir)
handler.process_images()
