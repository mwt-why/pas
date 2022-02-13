import time
from script.base_script import BaseScript
from script.ty.const import METHOD_LOOP_MAX_COUNT

package_name = 'com.netease.pm02'


class CheckoutAccount(BaseScript):
    is_ok = 0

    start_loop = 0

    def stuck_handle(self):
        self.start()

    def start(self):
        self.d.app_stop(package_name)
        time.sleep(3)
        self.d.app_start(package_name)
        time.sleep(35)
        return 'checkout_account'

    def always(self):
        box = self.get_like_word_box("更新公告")
        if box:
            self.click_x_y(1880, 84)

    checkout_account_loop_count = 0

    def checkout_account(self):
        if self.checkout_account_loop_count > METHOD_LOOP_MAX_COUNT:
            self.checkout_account_loop_count = 0
            return "start"
        time.sleep(9)
        box = self.get_word_box("账号")
        if box:
            self.click_box(box)
            return "choose_other_account"
        box = self.get_like_word_box("其他帐号登录")
        if box:
            self.click_box(box)
            return "click_agree"
        box = self.get_like_word_box("实名登记")
        if box:
            self.click_word("关闭")
        self.checkout_account_loop_count = self.checkout_account_loop_count + 1
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
        return "click_wy"  # 点击网易

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
        time.sleep(3)
        self.d.long_click(1080, 393, 4)
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
                return "click_start"
            else:
                self.is_ok = 1
                return "set_password"
        return "next"

    def set_password(self):
        password = self.task_data["password"]
        self.d.set_clipboard(password)
        self.d.clipboard
        self.d.click(1080, 393)
        time.sleep(3)
        self.d.long_click(1080, 393, 4)
        return "paste"

    def click_start(self):
        box = self.get_like_word_box("开始游戏")
        if box:
            self.click_box(box)
            time.sleep(9)
            return "end"
        box = self.get_like_word_box("登录")
        if box:
            return "account_exception"
        box = self.get_like_word_box("实名登记")
        if box:
            self.click_word("关闭")
            return "account_exception"
        return "click_start"
