from word.ocr_type import EASY_OCR
from word.my_easy_ocr import MyEasyOcr


class Ocr:
    def ocr(self, path):
        pass

    @staticmethod
    def get_ocr(ocr_type):
        if ocr_type == EASY_OCR:
            return MyEasyOcr()
