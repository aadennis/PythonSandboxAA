# Organize PNG files into a 'Screenshots' folder within each directory in OneDrive.
# This script assumes that most PNG files are screenshots (80/20 rule).
# It scans through all directories under the specified root folder (OneDrive) and:
# - Identifies PNG files in each directory.
# - Moves them into a 'Screenshots' subfolder within the same directory.
# - Skips directories that are already named 'Screenshots'.
# - Provides a dry-run mode to preview actions without making changes.

import os
import shutil

# Root directory to scan (set to your OneDrive root folder)
ROOT = r'c:/onedrive'

# Dry-run mode: Set to True to preview actions without making changes.
# Set to False to actually move files.
DRY_RUN = True

# Counter to track the total number of PNG files identified for moving
total_candidates = 0

# Walk through all directories and files under the root directory
for dirpath, dirnames, filenames in os.walk(ROOT):
    # Skip directories already named 'Screenshots' to avoid reprocessing
    if os.path.basename(dirpath).lower() == 'screenshots':
        continue

    # Identify all PNG files in the current directory
    png_files = [f for f in filenames if f.lower().endswith('.png')]
    if png_files:
        # Increment the total count of PNG files identified
        total_candidates += len(png_files)

        # Define the target 'Screenshots' folder path
        screenshots_dir = os.path.join(dirpath, 'Screenshots')

        # Dry-run: Preview folder creation
        if DRY_RUN:
            print(f"\nWould create (if not exists): {screenshots_dir}")
        else:
            # Create the 'Screenshots' folder if it doesn't already exist
            os.makedirs(screenshots_dir, exist_ok=True)

        # Process each PNG file in the current directory
        for png_file in png_files:
            # Define the source and target file paths
            src = os.path.join(dirpath, png_file)
            target = os.path.join(screenshots_dir, png_file)

            # Check if the target file already exists
            if os.path.exists(target):
                print(f"⚠️  WARNING: File already exists at target: {target}")
                continue

            # Dry-run: Preview file move
            if DRY_RUN:
                print(f"Would move: {src} -> {target}")
            else:
                # Move the file to the 'Screenshots' folder
                shutil.move(src, target)
                print(f"Moved: {src} -> {target}")

# Print the total number of PNG files identified for moving
print(f"\nTotal PNG files that are candidates for moving: {total_candidates}")

