import uiautomator2 as u2
import cv2

image_path = '../images/cur_image.jpg'

d = u2.connect_wifi('192.168.31.184')
image = d.screenshot(format='opencv')
cv2.imwrite(image_path, image)
