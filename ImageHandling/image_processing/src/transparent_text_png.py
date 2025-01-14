# https://chatgpt.com/c/6786ab39-86c8-8011-b432-1a128886ad6e

from PIL import Image, ImageDraw, ImageFont

def create_text_image(text, transparency=True, font="arial.ttf", font_size=72, output_file="output.png", corner_radius=20):
    """
    Creates an image with the given text, optionally with a transparent background and rounded corners.

    Parameters:
        text (str): The text to render in the image.
        transparency (bool): If True, the background is transparent. Otherwise, it's white.
        font (str): Font file name to use (located in c:/windows/fonts).
        font_size (int): Size of the font.
        output_file (str): Path to save the output image.
        corner_radius (int): Radius of the rounded corners for the background.

    Returns:
        None
    """
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

    # Determine the background color
    bg_color = (255, 255, 255, 255) if not transparency else (0, 0, 0, 0)

    # Create the image
    image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))  # Start with transparent image
    draw = ImageDraw.Draw(image)

    # Draw a rounded rectangle background
    rect_color = (255, 255, 255, 255) if not transparency else (200, 200, 200, 128)  # Slightly transparent gray for visualization
    draw.rounded_rectangle(
        [(0, 0), (image_width, image_height)],
        radius=corner_radius,
        fill=rect_color
    )

    # Draw the text
    draw.text((padding, padding), text, fill="black", font=font)

    # Save the image
    image.save(output_file)
    print(f"Image saved as {output_file}")

# Example Usage
create_text_image("This is a test", transparency=True, output_file="output_transparent.png", corner_radius=30)  # Transparent background
create_text_image("Another test", transparency=False, output_file="output_white_bg.png", corner_radius=30)  # White background
