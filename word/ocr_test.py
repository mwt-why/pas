import cv2
import easyocr
import numpy as np


def orc():
    path = "../images/7s.png"
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(path)
    print(result[0][1])
    for t in result:
        print(t)


def cv():
    a = [12, 3, 4, 56, 6]
    arr = np.array(a)
    cv2.connectedComponentsWithStats(arr.astype(np.uint8), connectivity=4)


orc()


def is_contain_num():
    import re
    s = "后面"
    print(bool(re.search(r'\d', s)))

# is_contain_num()
