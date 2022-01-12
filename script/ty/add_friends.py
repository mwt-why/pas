import time

from script.base_script import BaseScript
from server.router import Router


class AddFriends(BaseScript):
    router = Router()
    friends = ["司空语芙", "可怜小鱼"]

    def start(self):
        self.click_x_y(579, 990)
        return 'friend'

    def list_friends(self):
        params = {
            "roleName": self.task_data["role_name"],
            "area": self.task_data["area"]
        }
        self.friends = self.router.list_role_except_me(params)

    def friend(self):
        box = self.get_like_word_box('添加好友')
        if box:
            self.click_box(box)
            return 'pre_add_friends'
        return 'friend'

    def pre_add_friends(self):
        box = self.get_like_word_box('好友推荐')
        if box:
            self.click_box(box)
            return "add_friends"
        return "pre_add_friends"

    def add_friends(self):
        for f in self.friends:
            self.add_friend(f)
        return "end"

    def add_friend(self, role_name):
        self.d.set_clipboard(role_name)
        self.d.clipboard
        self.click_x_y(423, 162)  # 输入框
        time.sleep(1)
        self.click_x_y(1000, 500)  # 粘贴
        time.sleep(1)
        self.click_x_y(1873, 1000)  # 打钩确定
        time.sleep(1)
        self.click_x_y(630, 160)  # 点击搜索
        time.sleep(2)
        self.click_x_y(400, 300)  # 选中搜索出的内容
        time.sleep(2)
        self.click_x_y(1735, 985)  # 添加好友按钮
        time.sleep(1)
        self.click_x_y(574, 160)  # 清除搜索框内容


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '一世忆南',
          'task': 'rc', 'area': '长歌行', 'type': '0', 'mac': 'xd1', 'serial': '936X1XHD9'}
start = AddFriends(config)
start.run()
