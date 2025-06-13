# Organize PNG files into a 'Screenshots' folder within each directory in OneDrive.
# This is all on the 80/20 assumption that most PNG files are screenshots.
# So this is a crude triage script. 

import os
import shutil

ROOT = r'c:/onedrive'  # Your OneDrive root
DRY_RUN = True          # Set to False to perform actual moves

for dirpath, dirnames, filenames in os.walk(ROOT):
    # Skip already-handled folders
    if os.path.basename(dirpath).lower() == 'screenshots':
        continue

    # Get list of .png files in current folder
    png_files = [f for f in filenames if f.lower().endswith('.png')]
    if png_files:
        screenshots_dir = os.path.join(dirpath, 'Screenshots')

        if DRY_RUN:
            print(f"\nWould create (if not exists): {screenshots_dir}")
        else:
            os.makedirs(screenshots_dir, exist_ok=True)

        for png_file in png_files:
            src = os.path.join(dirpath, png_file)
            target = os.path.join(screenshots_dir, png_file)

            if os.path.exists(target):
                print(f"⚠️  WARNING: File already exists at target: {target}")
                continue

            if DRY_RUN:
                print(f"Would move: {src} -> {target}")
            else:
                shutil.move(src, target)
                print(f"Moved: {src} -> {target}")
