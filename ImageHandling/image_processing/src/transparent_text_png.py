# https://chatgpt.com/c/6786ab39-86c8-8011-b432-1a128886ad6e
from PIL import Image, ImageDraw, ImageFont

# Constants
TEXT = "This is a test"
FONT_PATH = "ttf_fonts/DejaVuSans-Bold.ttf"  
FONT_SIZE = 72  
TEXT_COLOR = "black"
OUTPUT_FILE = "output.png"

# Create a font object
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

# Calculate text size
dummy_image = Image.new("RGBA", (1, 1))  # Dummy image for textbbox calculation
dummy_draw = ImageDraw.Draw(dummy_image)
text_bbox = dummy_draw.textbbox((0, 0), TEXT, font=font)

# Get text dimensions from the bounding box
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Add some padding
padding = 10
image_width = text_width + 2 * padding
image_height = text_height + 2 * padding

# Create a transparent image
image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))

# Draw the text onto the image
draw = ImageDraw.Draw(image)
draw.text((padding, padding), TEXT, fill=TEXT_COLOR, font=font)

# Save the image
image.save(OUTPUT_FILE)

print(f"Image saved as {OUTPUT_FILE}")
