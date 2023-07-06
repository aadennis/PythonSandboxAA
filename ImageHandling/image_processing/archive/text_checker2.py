# https://github.com/UB-Mannheim/tesseract/wiki
import cv2
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

for i in range(3, 5):  # Assuming you have 10 images from a01.jpg to a10.jpg
    image_path = f'tests/a{i:02d}.jpg'  # Assuming the images are in the same directory as your Python script
    image2 = f'tests/out_{i:02d}.jpg'


    #Read the image using OpenCV
    #image = cv2.imread(image_path) # orig
    # Convert the image to grayscale
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # orig
    # Apply OCR using Pytesseract
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
    #print(data)

    cv2.imshow('thresh', thresh)
    cv2.imshow('opening', opening)
    cv2.imshow('invert', invert)
    #cv2.waitKey()
     # Check if text was detected or not
    if data:
        print(f'{image_path} contains text.')
    else:
        print(f'{image_path} does not contain text.')
    #text = pytesseract.image_to_string(Image.open(image_path), lang='eng', 
     #                                  config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789') # orig

    # im = Image.open(image_path)
    # im = im.filter(ImageFilter.MedianFilter())
    # enhancer = ImageEnhance.Contrast(im)
    # im = enhancer.enhance(2)
    # im = im.convert('1')
    # im.save(image2)
    # text = pytesseract.image_to_string(Image.open(image2))
    # print(text)




    #text = pytesseract.image_to_osd(gray)
    

   
