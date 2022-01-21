import time

from script.base_script import BaseScript
from script.ty.const import SURE


class CheckoutRole(BaseScript):

    def start(self):
        self.click_x_y(2075, 335)  # 点击菜单
        time.sleep(2)
        self.click_x_y(2000, 853)  # 点击设置
        return "click_checkout"

    def click_checkout(self):
        box = self.get_like_word_box("切换角色")
        if box:
            self.click_box(box)
            return "click_sure"
        return "click_checkout"

    def click_sure(self):
        self.click_image(SURE)
        time.sleep(3)
        box = self.get_like_word_box("开启云垂")
        if box:
            return "role_pag"
        return "click_sure"

    def role_pag(self):
        content = self.get_content(1, 3, 5)
        roles = self.get_roles(content)
        enter = self.task_data["enter"]
        for r in roles:
            if r[1] not in enter.done_role:
                self.click_box(r[0])
                enter.cur_role = r[1]
                enter.done_role.append(r[1])
                break
        return "start_yc"

    def start_yc(self):
        box = self.get_like_word_box("开启云垂")
        if box:
            self.click_box(box)
            return "end"
        return "start_yc"

    # ----------------以上结束-------------------------------------
    def mian_page(self):
        self.click_like_word("稍后")
        self.click_like_word("取消")
        box = self.get_like_word_box("前去找回")
        if box:
            self.click_x_y(1654, 300)
        box = self.get_like_word_box("我知道了")
        if box:
            self.click_x_y(1654, 300)
        if self.check_main_page():
            return "end"
        return "mian_page"

    @staticmethod
    def get_roles(content):
        roles = []
        for c in content:
            if "LV" not in c[1]:
                roles.append(c)
        return roles

    def check_main_page(self):
        self.click_x_y(72, 802)
        time.sleep(3)
        box = self.get_like_word_box('自动')
        if box:
            return True
        return False
