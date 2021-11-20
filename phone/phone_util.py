import uiautomator2 as u2
import cv2

image_path = '/home/why/dataset/cur_image/cur_image.jpg'

d = u2.connect('emulator-5554')
# d = u2.connect_wifi('10.0.2.16')
image = d.screenshot(format='opencv')
cv2.imwrite(image_path, image)

