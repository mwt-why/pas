import time

from script.base_script import BaseScript
from script.ty.const import BOX
from photo.cut import cut, generate_filename

money_area = ((0, 125), (1164, 1420))
max_loop_count = 2


class Statistics(BaseScript):
    swipe_up_count = 0
    swipe_up_max = 2
    swipe_down_count = 0
    swipe_down_max = 7
    close_join_gh_check = 1  # 表示没有点击，0表示已经点击了

    def start(self):
        self.click_x_y(1966, 341)
        return 'find_box'

    def always(self):
        if self.close_join_gh_check:
            if self.get_like_word_box("加入公会") is not None:
                self.click_x_y(968, 660)
                time.sleep(1)
                self.click_x_y(1511, 302)

    def find_box(self):
        if self.swipe_down_count >= self.swipe_down_max:
            return "statistics"
        self.click_x_y(2065, 300)  # 防止点错其他地方
        self.click_image(BOX)
        time.sleep(3)
        self.shot_screen()
        box = self.get_like_word_box("活跃度日常补给箱")
        if box:
            return "open_box"
        else:
            self.click_x_y(608, 555)
        self.swipe()
        box = self.get_like_word_box("背包格位需要")
        if box:
            box = self.get_like_word_box("取消")
            if box:
                self.click_box(box)
                return "statistics"
        return "find_box"

    def swipe(self):
        if self.swipe_up_count < self.swipe_up_max:
            self.d.swipe_ext("up", box=(1300, 871, 1640, 300))
            self.swipe_up_count = self.swipe_up_count + 1
        else:
            self.d.swipe_ext("down", box=(1300, 871, 1640, 300))
            self.swipe_down_count = self.swipe_down_count + 1
        time.sleep(1)

    def open_box(self):
        box = self.get_like_word_box("使用")
        if box:
            self.click_box(box)
            time.sleep(1)
            self.click_x_y(767, 707)
            return "set_max"
        return "open_box"

    def set_max(self):
        box = self.get_like_word_box("最大")
        if box:
            self.click_box(box)
            return "sure"
        return "set_max"

    def sure(self):
        box = self.get_like_word_box("确定")
        if box:
            self.click_box(box)
            return "get"
        return "sure"

    def get(self):
        box = self.get_like_word_box("领取")
        if box:
            self.click_box(box)
            return "use"
        return "get"

    def use(self):
        box = self.get_like_word_box("使用")
        if box:
            self.click_box(box)
            return "sure_use"
        return "use"

    count = 0  # 箱子只有一个的时候，没有确认按钮

    def sure_use(self):
        if self.count > 5:
            return "statistics"
        box = self.get_like_word_box("确定")
        if box:
            self.click_box(box)
            time.sleep(15)
            return "statistics"
        self.count = self.count + 1
        return "sure_use"

    statistics_loop_count = 0

    def statistics(self):
        money_path = generate_filename(self.image_path, "s")
        cut(self.image_path, money_area, money_path)
        result = self.ocr(money_path)
        print("检测统计结果", result)
        if len(result) == 0:
            self.record("0")
        else:
            self.record(result[0][1])
        self.click_x_y(97, 47)
        return "end"

    @staticmethod
    def is_num_head(s):
        import re
        return bool(re.search(r'\d', s))

    def record(self, money):
        enter = self.task_data["enter"]
        index = int(enter.role_index)
        role_info = enter.roles[(index - 1)]
        role = role_info[1]
        enter.statistics_result[role] = money
