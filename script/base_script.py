"""
每个实际的业务脚本必须继承该类
"""
import uiautomator2 as u2
import cv2
import time
import random
from env.env import Env
from photo.match_image import match

# 退出
EXIT = 1
# 重新开始
RESTART = 2
# 账号异常
ACCOUNT_EXCEPTION = 3
# 方法最大循环次数
METHOD_LOOP_MAX = 40


class BaseScript:
    d = None
    task_data = None
    image_path = None
    state = 0  # 0:未进入游戏，１:游戏中，2:游戏结束
    pre_enter_count = 0
    cur_env = None
    request_q = None
    receive_q = None
    is_new = False  # 是否是新的orc结果
    ocr_result_cache = []  # ocr结果缓存
    cur_method_count = 0
    cur_method = "start"

    def __init__(self, task_data):
        self.init_env()
        self.task_data = task_data
        self.connect(task_data)
        self.init_image_path(task_data)
        self.request_q = task_data['request_q']
        self.receive_q = task_data['receive_q']

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

    def ocr(self, path=None):
        if self.is_new:
            return self.ocr_result_cache
        if path is None:
            path = self.image_path
        self.request_q.put(path, block=True)
        while True:
            if self.receive_q.empty():
                time.sleep(0.5)
                continue
            self.is_new = True
            self.ocr_result_cache = self.receive_q.get()
            return self.ocr_result_cache

    def start(self):
        """
           留给子类实现
        """
        pass

    def always(self):
        pass

    def run(self):
        method_name = self.start()
        while True:
            self.shot_screen()
            method = getattr(self, method_name)
            print("当前方法：", method_name)
            method_name = method()
            result = self.always()
            if result is EXIT:
                time.sleep(3)
                return EXIT
            elif result is RESTART:
                return self.start()
            if method_name == 'end':
                time.sleep(3)
                return EXIT
            elif method_name == "account_exception":
                return ACCOUNT_EXCEPTION
            time.sleep(1)
            self.is_new = False
            if self.check_method(method_name):
                self.start()

    def check_method(self, new_method):
        """
        方法检测，主要解决卡死后的处理
        :param new_method:
        :return:
        """
        flag = 0
        if new_method == self.cur_method:
            self.cur_method_count = self.cur_method_count + 1
        else:
            self.cur_method_count = 0
            self.cur_method = new_method
        if self.cur_method_count > METHOD_LOOP_MAX:
            print("启用卡死检测方法")
            self.stuck_handle()
            self.cur_method_count = 0
            flag = 1
        return flag

    def stuck_handle(self):
        """
        卡死处理方法，子脚本可自己实现
        :return:
        """
        pass

    def shot_screen(self):
        """
            使用uiautomator2工具自带的api截屏
        """
        image = self.d.screenshot(format='opencv')
        cv2.imwrite(self.image_path, image)

    def shot_screen0(self, path=None):
        """
        借助adb截屏
        """
        self.d.shell("screencap /sdcard/screen.png")
        if path is None:
            path = self.image_path
        self.d.pull("/sdcard/screen.png", path)

    @staticmethod
    def drop_space(s):
        return s.replace(" ", "")

    def get_word_box(self, word, index=1):
        """
            获取指定具体文字的坐标
            :param word,需要获取坐标的文字
            :param index,如果有多个word匹配上,index表示需要顺序,默认是第一个
            :return box,文字的坐标
        """
        count = 1
        result = self.ocr()
        for r in result:
            s = self.drop_space(r[1])
            if word == s:
                if count == index:
                    print(word, r[0])
                    return r[0]
                count += 1
        return None

    def click_box(self, box):
        """
        随机点坐标内的点
        :param box,坐标
        """
        x = box[2][0] - box[0][0]
        y = box[2][1] - box[0][1]
        rx = random.randint(0, x)
        ry = random.randint(0, y)
        x = box[0][0] + rx
        y = box[0][1] + ry
        self.d.click(int(x), int(y))

    def click_x_y(self, x, y):
        """
        点击指定的坐标点
        :param x,表示点击坐标的x
        :param y,表示点击坐标的y
        """
        self.d.click(x, y)

    def click_word(self, word, index=1):
        """
        直接点击中匹配上的文字
        :param word,想要点击的文字
        :param index,下表,从1开始
        """
        box = self.get_word_box(word, index)
        if box is not None:
            self.click_box(box)

    def click_word_list(self, words, like=False):
        """
        想要点击多个word，如果匹配上就直接点击
        :param words,想要点击的文字集合
        """
        result = self.contain_words(words, like=like)
        if result is not None:
            box = result[0]
            self.click_box(box)
            return box
        else:
            return None

    def contain_words(self, word_list, like=False):
        """
        判断屏幕中是否包含，想要的文字的其中一个
        例如：['i','am','boy']，如果当前屏幕匹配上am，返回匹配结果
        :param word_list,想要匹配的文字集合
        :param like,是否采用模糊匹配,默认不采用
        :return 这是orc返回结果，注意不是box
        """
        result = self.ocr()
        for r in result:
            for w in word_list:
                if like:
                    if w in r:
                        return r
                else:
                    a = r[1]
                    a = self.drop_space(a)
                    if w in a:
                        return r[0]
        return None

    def get_like_word_box(self, word):
        """
        :param word,模糊匹配获取指定文字的坐标
        :return 文字box
        """
        result = self.ocr()
        for r in result:
            s = self.drop_space(r[1])
            if word in s:
                return r[0]
        return None

    def click_like_word(self, word):
        """
        直接点击模糊匹配上的文字
        :param word,指定的文字
        """
        box = self.get_like_word_box(word)
        if box:
            self.click_box(box)

    def walk_ahead(self, gap):
        """
        向前位移
        :param gap,位移步长
        """
        for i in range(gap):
            self.d.swipe_ext('up', box=(320, 500, 320, 850))

    def continuous_click(self, coordinate_list):
        """
        连续点击坐标
        :param coordinate_list,坐标元组集合
        """
        for (x, y) in coordinate_list:
            time.sleep(2)
            self.click_x_y(x, y)

    def count_word(self, word):
        """
        统计字的数量，精确匹配
        :param word,需要统计的字
        :return 字的数量
        """
        count = 0
        result = self.ocr()
        for r in result:
            if word in r:
                count += 1
        return count

    def count_like_word(self, word):
        """
            统计字的数量，模糊匹配
            :param word,需要统计的字
            :return 字的数量
        """
        count = 0
        result = self.ocr()
        for r in result:
            if word in r[1]:
                count += 1
        return count

    def match_image0(self, img):
        """
        图片对象检测
        :param img,被检测对象路径
        :return 图片相似度，和图片坐标
        """
        return match(self.image_path, img)

    def match_image(self, img):
        """
        图片对象检测
        :param img,被检测对象路径
        :return 图片坐标
        """
        result = self.match_image0(img)
        if result:
            return result['point'][0], result['point'][1]

    def click_image(self, img):
        """
        图片对象点击
        :param img,被点击图片的路径
        """
        x, y = self.match_image(img)
        self.d.click(x, y)

    def get_like_word_next_content(self, word):
        """
        获取指定文字的下一个被识别的文字的box
        :param 当前的文字
        :return 下一个文字的box
        """
        result = self.ocr()
        flag = False
        for r in result:
            if flag:
                return r
            if word in r[1]:
                flag = True
        return None

    def get_content(self, sort=0, offset=0, c=1):
        """
        :param sort,获取内容的顺序，０正序，１反序
        :param offset,开始位置
        :param c,获取的内容条数
        """
        content = []
        result = self.ocr()
        if sort:
            result = reversed(result)
        index = 0
        for r in result:
            if len(content) >= c:
                break
            if index < offset:
                index = index + 1
                continue
            content.append(r)
            index = index + 1
        return content
