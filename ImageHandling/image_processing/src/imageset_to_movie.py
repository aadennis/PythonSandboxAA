# https://chatgpt.com/c/677cb2e8-0dd0-8011-9dd2-b721c294fc3e
# VScode env latest:
# https://github.com/microsoft/vscode-python/wiki/Activate-Environments-in-Terminal-Using-Environment-Variables

import os
from moviepy import ImageClip, TextClip, concatenate_videoclips

# Path to the folder containing images
image_folder = "C:/temp/ImageDump/Ancestors2012"

# Duration for each image (in seconds)
image_duration = 4

# Title page text and duration
title_text = "My Awesome Slideshow"
title_duration = 4

# Get a list of all image files in the folder
valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif")
image_files = [
    os.path.join(image_folder, f)
    for f in sorted(os.listdir(image_folder))  # Sort ensures alphabetical order
    if f.lower().endswith(valid_extensions)
]

# Check if the folder contains images
if not image_files:
    raise ValueError("No valid image files found in the specified folder.")

# Create the title page clip
title_clip = (
    TextClip(title_text, fontsize=70, color="white", bg_color="black", size=(1280, 720))
    .set_duration(title_duration)
)

# Create a video clip for each image
image_clips = [ImageClip(img).set_duration(image_duration) for img in image_files]

# Combine the title clip and image clips
final_clips = [title_clip] + image_clips
final_video = concatenate_videoclips(final_clips, method="compose")

# Write the video to a file
output_path = "output_with_title.mp4"
final_video.write_videofile(output_path, fps=30)

print(f"Video created successfully: {output_path}")
