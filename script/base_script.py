import uiautomator2 as u2
import logging as log
import cv2
import time
import random
import sys
sys.path.append('home/why/workspace/python/pas/word')
from wordUtil import easy_ocr
base_image_pathe = '/home/why/workspace/python/pas/images'


class BaseScript:
    d = None
    task_data = None
    image_path = None

    def __init__(self, task_data):
        self.task_data = task_data
        self.d = u2.connect_wifi(task_data['ip'])
        self.image_path = base_image_pathe + '/' + \
            task_data['id'] + '/'+'screen.jpg'

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
        image = self.d.screenshot(format='opencv')
        cv2.imwrite(self.image_path, image)

    def get_word_box(self, word):
        result = easy_ocr(self.image_path)
        for r in result:
            if word in r:
                return [0]
        return None

    def click_box(box):
        x = box[3][0] - box[0][0]
        y = box[3][1] - box[0][1]
        rx = random.randint(0, x)
        ry = random.randint(0, y)
        x = box[0][0] + rx
        y = box[0][1] + ry
        d.click(x, y)
