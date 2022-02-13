import cv2

import numpy as np


def photo_different(filename1, filename2):
    image1 = cv2.imread(filename1)
    image2 = cv2.imread(filename2)
    difference = cv2.subtract(image1, image2)
    return not np.any(difference)  # if difference is all zeros it will return False
