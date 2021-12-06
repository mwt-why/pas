from script.base_script import BaseScript
import time

# ０表示还没有点，１表示已经点过
coo_dict = {(335, 305): '0', (598, 241): '0', (850, 301): '0', (1100, 231): '0',
            (1337, 331): '0', (300, 511): '0', (560, 590): '0', (860, 540): '0',
            (1130, 580): '0'}


#  家园
class JY(BaseScript):
    def start(self):
        self.click_x_y(1212, 860)
        return 'home_select'

    def home_select(self):
        box = self.get_like_word_box('随机选择')
        if box is not None:
            self.click_x_y(985, 430)
        box = self.get_like_word_box('回到世界')
        if box is not None:
            return 'pre_go_home'
        return 'home_select'

    def pre_go_home(self):
        box = self.get_like_word_box('美观家园展示')
        if box:
            self.click_box(box)
            coo = self.get_home_coo()
            if coo:
                self.click_x_y(coo[0], coo[1])
                return 'go_home'
        return 'pre_go_home'

    def go_home(self):
        box = self.get_like_word_box('参观家园')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('申请拜访')
        if box is not None:
            self.click_x_y(1243, 776)
            return 'visit'
        return 'go_home'

    def visit(self):
        box = self.get_word_box('社区')
        if box is not None:
            self.click_box(box)
            return 'pre_go_home'
        return 'visit'

    def exit(self):
        box = self.get_word_box('参观纪念')
        if box is not None:
            self.click_x_y(1830, 135)
            box = self.get_like_word_box('确定退出')
            if box is not None:
                box = self.get_like_word_box('确定')
                self.click_box(box)
                return 'exit'

    @staticmethod
    def get_home_coo():
        for k in coo_dict.keys():
            if coo_dict[k] == '0':
                coo_dict[k] = '1'
                return k
        return None


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行', 'type': '1',
          'mac': 'fdsafa'}
start = JY(config)
start.run()
