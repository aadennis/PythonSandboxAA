# https://chatgpt.com/c/6786ab39-86c8-8011-b432-1a128886ad6e
"""
Create captions for use in video tutorials.
The user can vary text (mandatory), font, font size, colour (all optional).
Output is png, with the option for the background behind the text to 
be transparent or solid.
The fonts used are ttf, and are hard-coded to the Windows location of c:/windows/fonts.
"""

import os
from math import ceil
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
    "orange": (255, 165, 0, 255), 
    "blood_orange": (204, 85, 0, 255)
}

def create_text_image(text, transparency=True, font="arial.ttf", font_size=172, corner_radius=20, bg_color="white"):
    """
    Creates an image with the given text, optionally with a transparent background and rounded corners.

    Parameters:
        text (str): The text to render in the image.
        transparency (bool): If True, the background is transparent. Otherwise, it's white (or a specified color).
        font (str): Font file name to use (located in c:/windows/fonts).
        font_size (int): Size of the font.
        corner_radius (int): Radius of the rounded corners for the background.
        bg_color (str): Background color name (defaults to "white"). Choose from the COLOR_PALETTE dictionary.

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

    # Calculate descent space
    ascent, descent = font.getmetrics()

    # Add some padding for space around the text
    padding = 20
    image_width = text_width + 2 * padding
    image_height = text_height + descent + 2 * padding  # Adjust height based on descent

    # Determine the background color
    if bg_color not in COLOR_PALETTE:
        raise ValueError(f"Invalid color name '{bg_color}'. Choose from: {', '.join(COLOR_PALETTE.keys())}")

    # Create the image with the specified background color or transparent
    image = Image.new("RGBA", (image_width, image_height), COLOR_PALETTE["transparent"] if transparency else COLOR_PALETTE[bg_color])
    draw = ImageDraw.Draw(image)

    # Draw a rounded rectangle background
    rect_color = COLOR_PALETTE[bg_color] if not transparency else COLOR_PALETTE["transparent"]
    draw.rounded_rectangle(
        [(0, 0), (image_width, image_height)],
        radius=corner_radius,
        fill=rect_color
    )

    # Adjust vertical offset slightly to prevent text from being too low
    vertical_padding_offset = font_size / 10
    draw.text((padding, ceil(padding - vertical_padding_offset)), text, fill=COLOR_PALETTE["black"], font=font)

    # Save the image
    output_path = f"{OUTPUT_FOLDER}/{output_filename}"
    image.save(output_path)
    print(f"Image saved as [{output_path}]")

# Example Usage
create_text_image("This is a test", transparency=False, bg_color="orange", corner_radius=30)  # Solid orange background
create_text_image("Another test", transparency=False, bg_color="blood_orange", corner_radius=30)  # Solid blood orange background
