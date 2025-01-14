# https://chatgpt.com/c/6786ab39-86c8-8011-b432-1a128886ad6e

import os
from PIL import Image, ImageDraw, ImageFont

def sanitize_filename(text):
    """
    Sanitizes text to be used as a file name by replacing invalid characters with underscores.
    
    Parameters:
        text (str): The input text to sanitize.
    
    Returns:
        str: Sanitized text suitable for use in file names.
    """
    invalid_chars = r'<>:"/\|?*'
    return "".join(c if c not in invalid_chars else "_" for c in text).strip()

# Define a dictionary for color names
COLOR_PALETTE = {
    "white": (255, 255, 255, 255),
    "off_white": (245, 245, 245, 255),
    "transparent": (0, 0, 0, 0),
    "gray": (200, 200, 200, 128),  # Slightly transparent gray
    "black": (0, 0, 0, 255),
}

def create_text_image(text, transparency=True, font="arial.ttf", font_size=72, corner_radius=20):
    """
    Creates an image with the given text, optionally with a transparent background and rounded corners.

    Parameters:
        text (str): The text to render in the image.
        transparency (bool): If True, the background is transparent. Otherwise, it's white.
        font (str): Font file name to use (located in c:/windows/fonts).
        font_size (int): Size of the font.
        corner_radius (int): Radius of the rounded corners for the background.

    Returns:
        None
    """
    # Output folder
    OUTPUT_FOLDER = "output"
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Generate the output file name based on the text and transparency
    sanitized_text = sanitize_filename(text)
    suffix = "transparent" if transparency else "white_bg"
    output_filename = f"{sanitized_text}_{suffix}.png"

    # Create a font object
    FONT_ROOT = "c:/windows/fonts"
    FONT_PATH = f"{FONT_ROOT}/{font}"
    font = ImageFont.truetype(FONT_PATH, font_size)

    # Calculate text size, including descent
    dummy_image = Image.new("RGBA", (1, 1))  # Dummy image for textbbox calculation
    dummy_draw = ImageDraw.Draw(dummy_image)
    text_bbox = dummy_draw.textbbox((0, 0), text, font=font)

    # Get text dimensions
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate additional descent space
    ascent, descent = font.getmetrics()
    total_height = text_height + descent

    # Add some padding
    padding = 20
    image_width = text_width + 2 * padding
    image_height = total_height + 2 * padding

    # Create the image
    image = Image.new("RGBA", (image_width, image_height), COLOR_PALETTE["transparent"])  # Start with transparent image
    draw = ImageDraw.Draw(image)

    # Draw a rounded rectangle background
    rect_color = COLOR_PALETTE["gray"] if transparency else COLOR_PALETTE["white"]
    draw.rounded_rectangle(
        [(0, 0), (image_width, image_height)],
        radius=corner_radius,
        fill=rect_color
    )

    # Draw the text
    draw.text((padding, padding), text, fill=COLOR_PALETTE["black"], font=font)

    # Save the image
    output_path = f"{OUTPUT_FOLDER}/{output_filename}"
    image.save(output_path)
    print(f"Image saved as [{output_path}]")

# Example Usage
create_text_image("This is a test", transparency=True, corner_radius=30)  # Transparent background
create_text_image("Another test", transparency=False, corner_radius=30)  # White background
