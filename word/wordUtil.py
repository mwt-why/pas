import easyocr

reader = easyocr.Reader(['ch_sim'])


def easy_ocr(path):
    return reader.readtext(path)
