import pyscreenshot as ImageGrab
import codecs
from PIL import Image
import pytesseract

if __name__ == '__main__':
    while True:
        im = ImageGrab.grab(bbox=(280, 200, 960, 600))
        text = pytesseract.image_to_string(im)
        file = codecs.open('text.txt', "a", "utf-8")
        file.write(text)
        file.close()