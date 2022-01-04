from script.base_script import BaseScript
import time


#  装备更换
class ZBGH(BaseScript):
    def start(self):
        self.click_x_y(1978, 330)
        return 'ready'

    def ready(self):
        box = self.get_like_word_box('背包')
        if box is not None:
            self.click_x_y(1453, 185)
            return 'resolve_equip'
        return 'ready'

    def resolve_equip(self):
        self.click_x_y(1230, 320)

        return 'resolve_equip'

    def goback(self):
        box = self.get_like_word_box('退出')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('仓库')
        if box is not None:
            self.click_x_y(100, 76)
            return 'end'
        return 'goback'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行', 'type': '1',
          'mac': 'fdsafa'}
start = ZBGH(config)
start.run()
