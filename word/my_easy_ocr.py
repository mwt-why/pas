from word.ocr import Ocr
import easyocr
import time


class MyEasyOcr(Ocr):
    reader = easyocr.Reader(['ch_sim', 'en'])
    lock = 0

    def ocr(self, path):
        while self.lock:
            time.sleep(2)
        self.__lock__()
        result = self.reader.readtext(path)
        self.__release_lock__()
        return result

    def __lock__(self):
        self.lock = 1

    def __release_lock__(self):
        self.lock = 0
