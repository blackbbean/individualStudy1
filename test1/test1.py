from PIL import Image
from pytesseract import *

def OCR(imgfile, lang='eng'):
    im = Image.open(imgfile)
    text = image_to_string(im,lang=lang)

    print('+++ RESULT +++')
    print(text)

OCR('ocr_test.jpg')