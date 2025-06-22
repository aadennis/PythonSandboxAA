"""
Organize HTML files and their associated _files folders into separate directories.
This script assumes that each HTML file has a corresponding folder named <filename>_files
which contains related resources (like images, stylesheets, etc.). 
"""

import os
import shutil

# Define the root directory
root = "C:/temp/webpage_triage"

# List everything in the directory
for item in os.listdir(root):
    if item.lower().endswith(".html"):
        html_path = os.path.join(root, item)
        base_name = os.path.splitext(item)[0]
        folder_name = base_name + "_files"
        folder_path = os.path.join(root, folder_name)
        destination = os.path.join(root, base_name)

        # Create destination folder if it doesn't exist
        os.makedirs(destination, exist_ok=True)

        # Move the .html file
        shutil.move(html_path, os.path.join(destination, item))

        # Move the _files folder if it exists
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            shutil.move(folder_path, os.path.join(destination, folder_name))

