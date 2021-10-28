import easyocr

reader = easyocr.Reader(['ch_sim'])
path = '/home/why/workspace/python/pas/word/1.jpeg'


def easy_ocr(path):
    return reader.readtext(path)
