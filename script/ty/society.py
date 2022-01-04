import time

from script.base_script import BaseScript


#  加工会
class JGH(BaseScript):
    @staticmethod
    def start():
        return 'join'

    def join(self):
        box = self.get_like_word_box('菜单')
        if box is not None:
            self.click_box(box)
            time.sleep(2)
        box = self.get_like_word_box('公会')
        if box is not None:
            self.click_box(box)
            return 'join_in'
        return 'join'

    def inspect(self):
        box = self.get_word_box('公会事件')
        if box is not None:
            return 'exit'
        return 'inspect'

    def join_in(self):
        box = self.get_like_word_box('键申请')
        if box is not None:
            self.click_box(box)
            return 'send'
        return 'join_in'

    def send(self):
        box = self.get_like_word_box('发送申请')
        if box is not None:
            self.click_box(box)
            return 'exit'
        return 'send'

    def exit(self):
        box = self.get_like_word_box('公会事件')
        if box is not None:
            self.click_x_y(100, 76)
            return 'end'
        return 'exit'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行', 'type': '1',
          'mac': 'fdsafa'}
start = JGH(config)
start.run()
