# Get any text in the single, given image.
# Words are not filtered for Englishness.
# Usage: Update the value for image_path in the code below. Then run.
# Output right now is just to the screen
#--------------------------------------------------------------------

# https://github.com/UB-Mannheim/tesseract/wiki
import cv2
import pytesseract
import colorama

# Highlight the passed string on the command line
def highlight(msg):
    colorama.init()
    print(colorama.Fore.BLUE + colorama.Back.YELLOW + msg)
    print()
    colorama.deinit()

def get_text_from_image(image_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    # Perform text extraction
    data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
    return data.split()
   
# main
image_path = f'tests/JulyTimes.jpg'  # Assuming the images are in the same directory as your Python script
image_text = get_text_from_image(image_path = image_path)
highlight(f"**** Printing any text found in [{image_path}] ****")
print(image_text)
