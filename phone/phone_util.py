import uiautomator2 as u2
import cv2

image_path = '/home/why/dataset/train/screenshot.jpg'

d = u2.connect()
image = d.screenshot(format='opencv')
cv2.imwrite(image_path, image)
