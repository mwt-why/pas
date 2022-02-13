from script.base_script import BaseScript
from script.ty.pre_start import PreStart
import time

package_name = 'com.netease.pm02'


class Start(BaseScript):

    def start(self):
        self.d.app_stop(package_name)
        time.sleep(3)
        self.d.app_start(package_name)
        time.sleep(35)
        return 'start_game'

    def always(self):
        box = self.get_like_word_box("更新公告")
        if box:
            self.click_x_y(1880, 89)

    def start_game(self):
        box = self.get_word_box('开始游戏')
        if box:
            self.click_box(box)
            return 'pre_start'
        return 'start_game'

    def pre_start(self):
        PreStart(self.task_data).run()
        return "end"
