import os
import subprocess
import shutil
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path 

# Function to extract creation date from EXIF data
def get_creation_date(file_path):
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


# Function to write text on image
def write_on_image(image_path, text, font_size=36):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)


    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)

    # Specify the position to draw the text
    text_position = (10, 10)
    
    # Draw the text on the image
    draw.text(text_position, text, (237, 230, 211), font=font)

    image.save(image_path)

# source_dir = '/Users/den/Downloads/picsamples' # Mac
# destination_dir = '/Volumes/MARKTEST/DennisPhotos' # Mac


print("File Path:", Path(__file__).absolute()) 
print("Directory Path:", Path().absolute())


source_dir = 'ImageHandling/tests/TestImageFiles' # PC
destination_dir = 'd:/Sandbox/git/aadennis/PythonSandboxAA/TestOutput' # Pc

# Dictionary to store counts of photos added to each folder
photos_added_counts = {}

# Iterate over each file in the source directoryc
for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)
    
    # Check if the file is a JPEG or JPG
    if file_name.lower().endswith(('.jpeg', '.jpg')):
        # Get creation date of the file
        try:
            creation_date = get_creation_date(file_path)
            print(creation_date)
            
            # Write creation date on image
            creation_date_str = creation_date.strftime('%Y-%m-%d')
            write_on_image(file_path, creation_date_str, font_size=72)
            
            # Construct destination folder path
            year_folder = creation_date.strftime('%Y')
            month_folder = creation_date.strftime('%Y-%m')
            destination_folder = os.path.join(destination_dir, year_folder, month_folder)
            
            # Create destination folder if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)
            
            # Copy file to destination folder
            shutil.copy2(file_path, destination_folder)
            
            # Increment count of photos added to destination folder
            photos_added_counts[destination_folder] = photos_added_counts.get(destination_folder, 0) + 1
        except Exception as e:
            print(f"Failed to get creation date for {file_path}: {e}")

# Print counts of photos added to each folder
print("Counts of photos added to each folder:")
for folder, count in photos_added_counts.items():
    print(f"{folder}: {count} photos")

print("Photo files have been copied to the appropriate folders.")
