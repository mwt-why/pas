iport uiautomator2 as u2
import cv2

image_path = '/home/why/workspace/python/pas/images/0/screen.jpg'

d = u2.connect()
image = d.screenshot(format='opencv')
cv2.imwrite(image_path, image)
