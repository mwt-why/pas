import easyocr
import time


class MyOcr(object):
    reader = easyocr.Reader(['ch_sim', 'en'])

    def __init__(self):
        self.lock = 0

    def ocr(self, path):
        while self.lock:
            time.sleep(2)
        self.lock = 1
        result = self.reader.readtext(path)
        self.lock = 0
        return result
