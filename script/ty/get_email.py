import time

from script.base_script import BaseScript
from script.ty.pre_start import PreStart


class GetEmail(BaseScript):
    # 如果出现卡死就去执行首页的弹框检测
    def stuck_handle(self):
        PreStart(self.task_data).run()

    def start(self):
        self.click_x_y(796, 892)
        return "get"

    def get(self):
        box = self.get_like_word_box("红包")
        if box:
            self.click_x_y(95, 50)
            return "start"
        box = self.get_like_word_box("键领取")
        if box:
            self.click_box(box)
            time.sleep(10)
            return "close_sure"
        return "get"

    def close_sure(self):
        self.click_word("确认")
        if self.get_word_box("使用"):
            self.click_x_y(1704, 566)
        box = self.get_like_word_box("键领取")
        if box:
            self.click_x_y(955, 540)
            time.sleep(3)
            return "close_use"
        return "close_sure"

    def close_use(self):
        if self.get_word_box("使用") or self.get_word_box("鉴定"):
            self.click_x_y(1704, 566)
            time.sleep(1)
            return "close_use"
        else:
            return "end"
