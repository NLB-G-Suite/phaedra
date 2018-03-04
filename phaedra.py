import pyscreenshot as ImageGrab
import codecs
from PIL import Image
import pytesseract
import time

class ChatAvenueScraper(object):
    def start(self, filename):
        while True:
            im = ImageGrab.grab(bbox=(280, 200, 1160, 600))
            text = pytesseract.image_to_string(im)
            file = codecs.open(filename, "a", "utf-8")
            file.write(text)
            file.close()
            time.sleep(0.05)

            
if __name__ == '__main__':
    scraper = ChatAvenueScraper()
    scraper.start('text8.txt')