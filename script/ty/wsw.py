from script.base_script import BaseScript
import time


# 万事屋
class Wsw(BaseScript):
    def start(self):
        self.click_x_y(478, 478)
        return 'wsw'

    def wsw(self):
        self.click_word('跳过')
        box = self.get_word_box('回去告诉无忌宝箱放好了')
        if box is not None:
            self.click_box(box)
            return 'pre_over'
        return 'wsw'

    def pre_over(self):
        self.click_word('跳过')
        box = self.get_word_box('使用')
        if box is not None:
            self.click_box(box)
            return 'exit'
        return 'pre_over'

    def exit(self):
        self.click_x_y(134, 1833)
        time.sleep(2)
        box = self.get_word_box('确定')
        if box is not None:
            self.click_box(box)
            return 'end'
        return 'exit'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
task = Wsw(config)
task.run()
