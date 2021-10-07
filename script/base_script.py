import uiautomator2 as u2
import logging as log
import cv2
import time

base_image_pathe = '/home/why/workspace/python/pas/images'


class BaseScript:
    dev_num = '0'
    ip = '0,0,0,0'
    d = None

    def __init__(self, ip, dev_num):
        self.ip = ip
        self.dev_num = dev_num
        self.d = u2.connect_wifi(ip)

    def start(self):
        log.warn("this is a abtract method,please implement it")

    def run(self):
        method_name = self.start()
        while(True):
            self.shot_screen()
            method = getattr(self, method_name)
            method_name = method()
            log.info('current method is:'+method_name)
            if method_name == 'end':
                break
            time.sleep(3)

    def shot_screen(self):
        image_path = base_image_pathe + '/' + self.dev_num + '/'+'screen.jpg'
        image = self.d.screenshot(format='opencv')
        cv2.imwrite(image_path, image)
