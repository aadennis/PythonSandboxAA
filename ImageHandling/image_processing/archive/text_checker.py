# https://github.com/UB-Mannheim/tesseract/wiki
import cv2
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

for i in range(1, 6):  # Assuming you have 10 images from a01.jpg to a10.jpg
    image_path = f'tests/a{i:02d}.jpg'  # Assuming the images are in the same directory as your Python script


    # Read the image using OpenCV
    image = cv2.imread(image_path)
    # im = Image.open(image_path)
    # im - im.filter(ImageFilter.MedianFilter())
    # enhancer = ImageEnhance.Contrast(im)
    # im = enhancer.enhance(2)
    # im = im.convert('1')
    # newfile = "x" + image_path
    # im.save(newfile)
    # text = pytesseract.image_to_string(Image.open(newfile))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply OCR using Pytesseract
    text = pytesseract.image_to_string(gray)
    #text = pytesseract.image_to_osd(gray)
    

    # Check if text was detected or not
    if text:
        print(f'{image_path} contains text.')
    else:
        print(f'{image_path} does not contain text.')
