from script.base_script import BaseScript
import time


class CurRole(BaseScript):
    def start(self):
        self.click_x_y(2075, 335)  # 点击菜单
        time.sleep(2)
        self.click_x_y(2000, 853)  # 点击设置
        return "get_role"

    def get_role(self):
        content = self.get_like_word_next_content("基础")
        if content:
            role = content[1]
            print("当前角色", role)
            enter = self.task_data["enter"]
            enter.role_index = role
            self.click_x_y(97, 55)
            time.sleep(3)
            return "end"
        return "get_role"
