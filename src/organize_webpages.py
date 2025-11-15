"""
Organize HTML files and their associated resource folders into separate directories.

This script processes HTML files in a root directory and:
- Creates a separate folder for each HTML file (named after the HTML file).
- Moves the HTML file into its corresponding folder.
- Moves the associated '_files' folder (containing resources like images, stylesheets, etc.) 
  into the same folder as the HTML file.

Useful for organizing downloaded web pages that come with resource folders.
"""

import os
import shutil

# Define the root directory containing HTML files and their associated folders
root = "C:/temp/webpage_triage"

# Iterate through all items in the root directory
for item in os.listdir(root):
    # Check if the item is an HTML file
    if item.lower().endswith(".html"):
        # Define the full path to the HTML file
        html_path = os.path.join(root, item)
        
        # Extract the base name without the .html extension
        base_name = os.path.splitext(item)[0]
        
        # Define the name of the associated '_files' folder
        folder_name = base_name + "_files"
        folder_path = os.path.join(root, folder_name)
        
        # Define the destination folder where HTML and resources will be organized
        destination = os.path.join(root, base_name)

        # Create the destination folder if it doesn't already exist
        os.makedirs(destination, exist_ok=True)

        # Move the HTML file to the destination folder
        shutil.move(html_path, os.path.join(destination, item))
        print(f"Moved: {item} → {destination}")

        # Move the associated '_files' folder if it exists
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            shutil.move(folder_path, os.path.join(destination, folder_name))
            print(f"Moved: {folder_name} → {destination}")

# Pause before exiting to allow the user to review the results
input("\nDone. Press Enter to exit...")
