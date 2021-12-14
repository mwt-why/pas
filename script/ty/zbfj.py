from script.base_script import BaseScript
import time


#  装备分解
class ZBFJ(BaseScript):
    def start(self):
        self.click_x_y(1978, 330)
        return 'ready'

    def ready(self):
        box = self.get_like_word_box('背包')
        if box is not None:
            self.click_x_y(1453, 185)
        box = self.get_like_word_box('分解')
        if box is not None:
            self.click_box(box)
            return 'resolve'
        return 'ready'

    def resolve(self):
        box = self.get_like_word_box('紫装及以下')
        if box is not None:
            self.click_x_y(1775, 170)
            time.sleep(5)
        box = self.get_like_word_box('一键分解')
        if box is not None:
            self.click_box(box)
            return 'goback'
        return 'resolve'

    def goback(self):
        box = self.get_like_word_box('退出')
        if box is not None:
            self.click_box(box)
            box = self.get_like_word_box('仓库')
            if box is not None:
                self.click_x_y(100, 767)
                return 'end'
        return 'goback'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行', 'type': '1',
          'mac': 'fdsafa'}
start = ZBFJ(config)
start.run()
