import time

from script.base_script import BaseScript
from script.ty.const import SURE
from script.ty.pre_start import PreStart


class CheckoutRole(BaseScript):

    # 如果出现卡死就去执行首页的弹框检测
    def stuck_handle(self):
        PreStart(self.task_data).run()

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
        enter = self.task_data["enter"]
        if enter.roles is not None:
            self.select_role()
            return "start_yc"
        content = self.get_content(c=5)
        roles = self.get_roles(content)
        print(roles)
        self.set_roles(roles)
        self.select_role()
        return "start_yc"

    def select_role(self):
        enter = self.task_data["enter"]
        role_info = enter.roles[enter.role_index]
        self.click_box(role_info[0])
        enter.role_index = enter.role_index + 1  # 角色下标加1

    def set_roles(self, roles):
        enter = self.task_data["enter"]
        enter.roles = roles

    def get_roles(self, content):
        roles = []
        for c in content:
            if c[1] == "删除角色":
                break
            if "LV" not in c[1] and "Lv" not in c[1]:
                roles.append(c)
        self.task_data["roleNum"] = len(roles)
        return roles

    def start_yc(self):
        box = self.get_like_word_box("开启云垂")
        if box:
            self.click_box(box)
            return "pre_start"
        return "start_yc"

    def pre_start(self):
        PreStart(self.task_data).run()
        time.sleep(3)
        return "end"
