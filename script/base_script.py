import uiautomator2 as u2
import logging as log
import cv2
import time
import random

from word.wordUtil import easy_ocr

base_image_path = '/home/why/workspace/python/pas/images'


class BaseScript:
    d = None
    task_data = None
    image_path = None
    state = 0  # 0:未进入游戏，１:游戏中，2:游戏结束
    pre_enter_count = 0

    def __init__(self, task_data):
        self.task_data = task_data
        self.d = u2.connect_wifi(task_data['ip'])
        self.image_path = base_image_path + '/' + task_data['id'] + '/' + 'screen.jpg'

    def run(self):
        method_name = self.start()
        while True:
            self.shot_screen()
            method = getattr(self, method_name)
            method_name = method()
            print('current method is:' + method_name)
            log.info('current method is:' + method_name)
            if method_name == 'end':
                break
            time.sleep(1)

    def shot_screen(self):
        image = self.d.screenshot(format='opencv')
        cv2.imwrite(self.image_path, image)

    def get_word_box(self, word, index=1):
        count = 1
        result = easy_ocr(self.image_path)
        for r in result:
            if word in r:
                if count == index:
                    print(word, r[0])
                    return r[0]
                count += 1
        return None

    def click_box(self, box):
        x = box[2][0] - box[0][0]
        y = box[2][1] - box[0][1]
        rx = random.randint(0, x)
        ry = random.randint(0, y)
        x = box[0][0] + rx
        y = box[0][1] + ry
        self.d.click(int(x), int(y))

    def click_x_y(self, x, y):
        self.d.click(x, y)

    def click_word(self, word, index=1):
        box = self.get_word_box(word, index)
        if box is not None:
            self.click_box(box)

    def click_word_list(self, words):
        result = self.contain_words(words)
        if result is not None:
            box = result[0]
            self.click_box(box)
            return box
        else:
            return None

    def close_modal(self, word_map, word_list):
        print('关闭弹出')
        result = easy_ocr(self.image_path)
        for r in result:
            for k in word_map.keys():
                if k in r:
                    x = word_map[k][0]
                    y = word_map[k][1]
                    self.click_x_y(x, y)
                    self.pre_enter_count += 1
                    return 0
            for w in word_list:
                if w in r:
                    self.click_box(r[0])
                    self.pre_enter_count += 1
                    return 0
            if self.task_data['role_name'] in r and self.pre_enter_count > 0:
                return 1
        return 2

    def contain_words(self, word_list):
        result = easy_ocr(self.image_path)
        for r in result:
            for w in word_list:
                if w in r:
                    return r
        return None

    def get_refX_box(self, word, ref_word, offset):
        result = easy_ocr(self.image_path)
        for r in result:
            if ref_word in r:
                ref_x = r[0][0][0]
                for rr in result:
                    if word in rr:
                        wx = rr[0][0][0]
                        wx_max = wx + offset
                        wx_min = wx - offset
                        if wx_min < ref_x < wx_max:
                            return rr[0]

        return None

    def get_like_word_box(self, word):
        result = easy_ocr(self.image_path)
        for r in result:
            if word in r[1]:
                return r[0]
        return None
