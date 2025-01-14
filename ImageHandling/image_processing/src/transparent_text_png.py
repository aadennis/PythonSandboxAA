# https://chatgpt.com/c/6786ab39-86c8-8011-b432-1a128886ad6e
from PIL import Image, ImageDraw, ImageFont

# Constants
TEXT = "This is a test"
FONT_PATH = "DejaVuSans-Bold.ttf"  # Adjust this to your font file path
FONT_SIZE = 36  # Font size
TEXT_COLOR = "black"
OUTPUT_FILE = "output.png"

# Create a font object
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

# Calculate text size
text_width, text_height = font.getsize(TEXT)

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

