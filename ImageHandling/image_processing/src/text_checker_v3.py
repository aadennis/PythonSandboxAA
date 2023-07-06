# https://github.com/UB-Mannheim/tesseract/wiki
import cv2
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import nltk

nltk.download('words')
english_words = set(nltk.corpus.words.words())

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

for i in range(1, 6):  # Assuming you have 10 images from a01.jpg to a10.jpg
    image_path = f'tests/a{i:02d}.jpg'  # Assuming the images are in the same directory as your Python script
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
    extracted_text = data
    words = extracted_text.split()
    filtered_words = [word for word in words if len(word) >= 4 and word.lower() in english_words]

    if filtered_words:
        print(f'{image_path} contains text.')
        print(filtered_words)
        print("-------------------------")
    else:
        print(f'{image_path} does not contain text.')
