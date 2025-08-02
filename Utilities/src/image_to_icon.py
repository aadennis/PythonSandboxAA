# Convert an image to ICO format using Pillow.
# AVIF: pillow-avif-plugin is not required on later versions of Pillow as
# Pillow now supports AVIF natively.

from PIL import Image
import os

def convert_to_ico(image_path):
    # Validate input
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Prepare output path
    base, _ = os.path.splitext(image_path)
    icon_path = f"{base}.ico"

    # Open and convert image
    img = Image.open(image_path)
    print(f"Loaded image: format={img.format}, size={img.size}, mode={img.mode}")


    img = img.convert("RGBA")  # Ensure image is in RGBA format
    img = img.resize((256, 256), Image.LANCZOS)  
    img.save(icon_path, format="ICO", sizes=[(256, 256)])

    print(f"Icon saved: {icon_path}")

if __name__ == "__main__":
    image = "C:\\temp\\downloads\\vthumb_300.jpg"
    convert_to_ico(image)