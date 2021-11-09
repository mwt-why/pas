import easyocr

reader = easyocr.Reader(['ch_sim', 'en'])


def easy_ocr(path):
    return reader.readtext(path)
