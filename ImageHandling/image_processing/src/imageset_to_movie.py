import os
#from moviepy.video.VideoClip import TextClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy import concatenate_videoclips
from moviepy import TextClip

font = "./PlayfairDisplaySemibold.ttf"

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

# # Create the title page clip
# title_clip = (
#     TextClip(title_text, font='Arial', font_size=70, color="white", bg_color="black", size=(1280, 720))
#     .set_duration(title_duration)
# )

# Create the title page clip
# title_clip = (
#     TextClip(title_text, fontsize=70, color="white", bg_color="black", size=(1280, 720))
#     .set_duration(title_duration)
# )

title_clip = (
    TextClip(
    font=font,
    filename="./example.txt",
    size=(500, 200),
    #bg_color="#FFFFFF",
    bg_color="white",
    method="caption",
    #color=(0, 0, 255, 127),
    color="black",
    margin=(20, 10)
).with_duration(title_duration))  # Blue with 50% transparency

# Create a video clip for the images
image_clip = ImageSequenceClip(image_files, durations=[image_duration] * len(image_files))

# Combine the title clip and image clip
final_video = concatenate_videoclips([title_clip, image_clip])

# Write the video to a file
output_path = "output_with_title.mp4"
final_video.write_videofile(output_path, fps=30)

print(f"Video created successfully: {output_path}")
