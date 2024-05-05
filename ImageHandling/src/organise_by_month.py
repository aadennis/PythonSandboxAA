import os
import shutil
from datetime import datetime

# Function to extract creation date of a file
def get_creation_date(file_path):
    creation_time = os.stat(file_path).st_birthtime
    return datetime.fromtimestamp(creation_time)

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

print("Photo files have been copied to the appropriate folders.")
