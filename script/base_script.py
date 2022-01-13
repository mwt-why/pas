"""
每个实际的业务脚本必须继承该类
"""
import uiautomator2 as u2
import cv2
import time
import random

from word.wordUtil import easy_ocr
from env.env import Env

EXIT = 0


class BaseScript:
    d = None
    task_data = None
    image_path = None
    state = 0  # 0:未进入游戏，１:游戏中，2:游戏结束
    pre_enter_count = 0
    cur_env = None

    def __init__(self, task_data):
        self.init_env()
        self.task_data = task_data
        self.connect(task_data)
        self.init_image_path(task_data)

    def init_env(self):
        self.cur_env = Env()

    def connect(self, task_data):
        # 判断设备类型,0:虚拟带serial，1物理:带ip
        d_type = task_data['type']
        if d_type == '0':
            serial = task_data['serial']
            self.d = u2.connect(serial)
        else:
            ip = task_data['ip']
            self.d = u2.connect_wifi(ip)

    def init_image_path(self, task_data):
        id = task_data['id']
        image_dir = self.cur_env.get_value('image.dir')
        img_type = self.cur_env.get_value('image.img_type')
        self.image_path = image_dir + id + "." + img_type

    """
    留给子类实现
    """

    def start(self):
        pass

    def run(self):
        method_name = self.start()
        while True:
            self.shot_screen()
            method = getattr(self, method_name)
            print("当前方法：", method)
            method_name = method()
            if method_name == 'end':
                return EXIT

    """
    使用uiautomator2工具自带的api截屏
    """

    def shot_screen0(self):
        image = self.d.screenshot(format='opencv')
        cv2.imwrite(self.image_path, image)

    """
    借助adb截屏
    """

    def shot_screen(self):
        self.d.shell("screencap /sdcard/screen.png")
        self.d.pull("/sdcard/screen.png", self.image_path)

    """
    获取指定具体文字的坐标
    :param word,需要获取坐标的文字
    :param index,如果有多个word匹配上,index表示需要顺序,默认是第一个
    :return box,文字的坐标
    """

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

    """
    随机点坐标内的点
    :param box,坐标
    """

    def click_box(self, box):
        x = box[2][0] - box[0][0]
        y = box[2][1] - box[0][1]
        rx = random.randint(0, x)
        ry = random.randint(0, y)
        x = box[0][0] + rx
        y = box[0][1] + ry
        self.d.click(int(x), int(y))

    """
    点击指定的坐标点
    :param x,表示点击坐标的x
    :param y,表示点击坐标的y
    """

    def click_x_y(self, x, y):
        self.d.click(x, y)

    """
    直接点击中匹配上的文字
    :param word,想要点击的文字
    :param index,下表,从1开始
    """

    def click_word(self, word, index=1):
        box = self.get_word_box(word, index)
        if box is not None:
            self.click_box(box)

    """
    想要点击多个word，如果匹配上就直接点击
    :param words,想要点击的文字集合
    """

    def click_word_list(self, words):
        result = self.contain_words(words)
        if result is not None:
            box = result[0]
            self.click_box(box)
            return box
        else:
            return None

    """
    判断屏幕中是否包含，想要的文字的其中一个
    例如：['i','am','boy']，如果当前屏幕匹配上am，返回匹配结果
    :param word_list,想要匹配的文字集合
    :return 这是orc返回结果，注意不是box
    """

    def contain_words(self, word_list):
        result = easy_ocr(self.image_path)
        for r in result:
            for w in word_list:
                if w in r:
                    return r
        return None

    """
    :param word,模糊匹配获取指定文字的坐标
    :return 文字box
    """

    def get_like_word_box(self, word):
        result = easy_ocr(self.image_path)
        for r in result:
            if word in r[1]:
                return r[0]
        return None

    """
    直接点击模糊匹配上的文字
    :param word,指定的文字
    """

    def click_like_word(self, word):
        box = self.get_like_word_box(word)
        if box:
            self.click_box(box)

    """
    向前位移
    :param gap,位移步长
    """

    def walk_ahead(self, gap):
        for i in range(gap):
            self.d.swipe_ext('up', box=(320, 500, 320, 850))

    """
    连续点击坐标
    :param coordinate_list,坐标元组集合
    """

    def continuous_click(self, coordinate_list):
        for (x, y) in coordinate_list:
            time.sleep(2)
            self.click_x_y(x, y)

    """
    统计字的数量，精确匹配
    :param word,需要统计的字
    :return 字的数量
    """

    def count_word(self, word):
        count = 0
        result = easy_ocr(self.image_path)
        for r in result:
            if word in r:
                count += 1
        return count

    """
        统计字的数量，模糊匹配
        :param word,需要统计的字
        :return 字的数量
        """

    def count_like_word(self, word):
        count = 0
        result = easy_ocr(self.image_path)
        for r in result:
            if word in r[1]:
                count += 1
        return count
