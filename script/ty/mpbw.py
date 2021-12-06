import time

from script.base_script import BaseScript


#  门派比武
class QlZY(BaseScript):
    def start(self):
        self.click_x_y(555, 555)
        return 'play'

    def play(self):
        self.click_word('开始匹配')
        box = self.get_like_word_box('提示')
        if box is not None:
            self.click_word('确定')
        box = self.get_like_word_box('匹配成功')
        if box is not None:
            return 'scan'
        return 'play'

    def scan(self):
        box = self.get_like_word_box('扫荡')
        if box is not None:
            self.click_box(box)
        box = self.get_word_box('确定')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('0次')
        if box is not None:
            return 'exit'
        return 'challenge'

    def challenge(self):
        box = self.get_like_word_box('扫荡')
        if box is not None:
            self.click_box(box)
            return 'scan'
        box = self.get_word_box('挑战')
        if box is not None:
            self.click_box(box)
            return 'pre_challenge'
        return 'challenge'

    def pre_challenge(self):
        box = self.get_like_word_box('挂机')
        if box is not None:
            self.click_box(box)
        time.sleep(2)
        box = self.get_like_word_box('自动战斗中')
        if box is not None:
            return 'do_challenge'
        return 'pre_challenge'

    def do_challenge(self):
        box = self.get_like_word_box('再次挑战')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('花费')
        if box is not None:
            box = self.get_like_word_box('取消')
            if box is not None:
                self.click_box(box)
                return 'exit'
        return 'do_challenge'

    def exit(self):
        box = self.get_like_word_box('返回')
        if box is not None:
            self.click_box(box)
            return 'end'
        return 'exit'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
task = QlZY(config)
task.run()
