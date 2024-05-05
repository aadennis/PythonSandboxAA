import os
import subprocess
import shutil
from datetime import datetime

# Function to extract creation date from EXIF data
def get_creation_date(file_path):
    exif_data = subprocess.check_output(['exiftool', '-CreateDate', '-d', '%Y-%m-%d %H:%M:%S', file_path]).decode('utf-8')
    creation_date_str = exif_data.split(': ')[1].strip()
    return datetime.strptime(creation_date_str, '%Y-%m-%d %H:%M:%S')

# Source directory containing photo files
source_dir = '/Users/den/Downloads/picsamples'

# Destination directory
destination_dir = '/Volumes/MARKTEST/DennisPhotos'

# Iterate over each file in the source directory
for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)
    
    # Check if the file is a JPEG or JPG
    if file_name.lower().endswith(('.jpeg', '.jpg')):
        # Get creation date of the file
        try:
            creation_date = get_creation_date(file_path)
            print(creation_date)
            
            # Construct destination folder path
            year_folder = creation_date.strftime('%Y')
            month_folder = creation_date.strftime('%Y-%m')
            destination_folder = os.path.join(destination_dir, year_folder, month_folder)
            
            # Create destination folder if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)
            
            # Copy file to destination folder
            shutil.copy2(file_path, destination_folder)
        except Exception as e:
            print(f"Failed to get creation date for {file_path}: {e}")

print("Photo files have been copied to the appropriate folders.")


