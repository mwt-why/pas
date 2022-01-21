from script.base_script import BaseScript
import time

package_name = 'com.netease.pm02'


class Start(BaseScript):
    is_ok = 0
    start_count = 0

    def start(self):
        self.d.app_stop(package_name)
        time.sleep(3)
        self.d.app_start(package_name)
        return 'select_area'

    def always(self):
        box = self.get_like_word_box("更新公告")
        if box:
            self.click_x_y(1880, 89)

    def is_new_account(self):
        if self.task_data["isNewAccount"]:
            return 'checkout_account'
        else:
            return 'select_area'

    def checkout_account(self):
        box = self.get_word_box("账号")
        if box:
            self.click_box(box)
            return "choose_other_account"
        return "checkout_account"

    def choose_other_account(self):
        self.click_word("切换帐号")
        box = self.get_like_word_box("其他帐号登录")
        if box:
            self.click_box(box)
            return "click_agree"
        return "choose_other_account"

    def click_agree(self):
        self.click_x_y(881, 826)
        return "click_wy"

    def click_wy(self):
        box = self.get_like_word_box("邮箱")
        if box:
            self.click_box(box)
            return "input_account"
        return "click_wy"

    def input_account(self):
        box = self.get_like_word_box("帐号")
        if box:
            self.click_box(box)
            return "set_clipboard"
        return "input_account"

    def set_clipboard(self):
        account = self.task_data["account"]
        self.d.set_clipboard(account)
        self.d.clipboard
        self.d.click(1080, 393)
        time.sleep(1)
        self.d.long_click(1080, 393, 2)
        return "paste"

    def paste(self):
        box = self.get_like_word_box("粘贴")
        if box:
            self.click_box(box)
            return "next"
        return "paste"

    def next(self):
        box = self.get_like_word_box("下一步")
        if box:
            self.click_box(box)
            if self.is_ok:
                self.task_data["isNewAccount"] = 0
                self.start_count = 0
                return "start"
            else:
                self.is_ok = 1
                return "set_password"
        return "next"

    def set_password(self):
        password = self.task_data["password"]
        self.d.set_clipboard(password)
        self.d.clipboard
        self.d.click(1080, 393)
        time.sleep(1)
        self.d.long_click(1080, 393, 2)
        return "paste"

    def select_area(self):
        account = self.task_data["account"]
        self.d.set_clipboard(account)
        area = self.task_data['area']
        box = self.get_word_box(area)
        if box is None:
            self.click_word('更换')
            pass
        return 'start_game'

    def start_game(self):
        time.sleep(5)
        box = self.get_like_word_box('公告')
        if box:
            self.click_x_y(1880, 89)
        box = self.get_word_box('开始游戏')
        if box:
            self.click_box(box)
            return 'pre_start'
        return 'start_game'

    def pre_start(self):
        self.click_word('开启云垂')
        box = self.get_word_box('今日不再弹出')
        self.click_word("稍后")
        if box:
            self.click_x_y(1985, 130)
        box = self.get_like_word_box("前去找回")
        if box:
            self.click_x_y(1654, 300)
            return 'boon_hall'
        box = self.get_like_word_box("我知道了")
        if box:
            self.click_box(box)
            return 'boon_hall'
        return 'pre_start'

    def click_comm_ft(self):
        box = self.get_like_word_box("签到")
        if box:
            self.click_box(box)
            self.click_x_y(1678, 230)
        box = self.get_word_box('普通找回')
        if box:
            self.click_box(box)
            return 'find_ret'
        return 'click_comm_ft'

    def find_ret(self):
        for i in range(10):
            time.sleep(2)
            self.click_word('花费')
        self.d.swipe_ext('up', box=(1359, 70, 1100, 1100))
        box = self.get_word_box('福利')
        if box:
            self.click_box(box)
            return 'get_boon'
        return 'find_ret'

    def get_boon(self):
        self.click_word('领取奖励')
        box = self.get_like_word_box("大厅")
        if box:
            self.click_box(box)
            return 'boon_hall'
        return 'get_boon'

    def boon_hall(self):
        self.click_like_word("取消")
        box = self.get_like_word_box("签到")
        if box:
            self.click_box(box)
            self.click_x_y(1678, 230)
        result = self.check_main_page()
        if result:
            return 'end'
        return 'boon_hall'

    def check_main_page(self):
        self.click_x_y(72, 802)
        box = self.get_like_word_box('自动')
        if box:
            return True
        return False
