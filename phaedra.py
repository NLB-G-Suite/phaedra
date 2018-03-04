import pyscreenshot as ImageGrab
import codecs
from PIL import Image
import pytesseract
import time

if __name__ == '__main__':
    while True:
        im = ImageGrab.grab(bbox=(280, 200, 1160, 600))
        text = pytesseract.image_to_string(im)
        file = codecs.open('text7.txt', "a", "utf-8")
        file.write(text)
        file.close()
        time.sleep(0.05)