# 出学院
from base_script import BaseScript
import time
package_name = 'com.netease.pm02'


class CXY(BaseScript):
    def start(self):
        self.d.app_stop(package_name)
        time.sleep(3)
        self.d.app_start(package_name)
        return 'start_game'

    def start_game(self):
        box = self.get_word_box('开始游戏')
        if box != None:
            self.click_box(box)
        return 'end'


config = {'id': '0', 'ip': '192.168.31.185'}
cxy = CXY(config)
cxy.run()
