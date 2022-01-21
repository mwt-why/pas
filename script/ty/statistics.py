import time

from script.base_script import BaseScript
from script.ty.const import BOX


class Statistics(BaseScript):
    swipe_up_count = 0
    swipe_up_max = 2
    swipe_down_count = 0
    swipe_down_max = 5

    def start(self):
        self.click_x_y(1966, 341)
        return 'find_box'

    def find_box(self):
        if self.swipe_down_count >= self.swipe_down_max:
            return "statistics"
        self.click_image(BOX)
        self.click_x_y(2065, 300)  # 防止点错其他地方
        time.sleep(3)
        self.shot_screen()
        box = self.get_like_word_box("活跃度日常补给箱")
        if box:
            return "open_box"
        else:
            self.click_x_y(608, 555)
        self.swipe()
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

    def sure_use(self):
        box = self.get_like_word_box("确定")
        if box:
            self.click_box(box)
            time.sleep(7)
            return "statistics"
        return "sure_use"

    def statistics(self):
        content = self.get_like_word_next_content("万")
        if content:
            print(content)
            self.record(content[1])
            self.click_x_y(100, 47)  # 返回
            return "end"
        return "statistics"

    def record(self, money):
        enter = self.task_data["enter"]
        role = enter.cur_role
        result = role + ":" + money
        enter.statistics_result.append(result)
