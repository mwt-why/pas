from script.base_script import BaseScript
from script.ty.const import CLOSE1, CLOSE2, CLOSE3
import time

package_name = 'com.netease.pm02'


class Start1(BaseScript):

    def start(self):
        self.d.app_stop(package_name)
        time.sleep(3)
        self.d.app_start(package_name)
        return 'pre_main'

    def pre_main(self):
        self.click_like_word("开始游戏")
        self.click_image(CLOSE1)
        self.click_image(CLOSE2)
        self.click_image(CLOSE3)
        self.click_like_word("开启云垂")
        self.click_like_word("取消")
        self.click_like_word("稍后")
        if self.check_main_page():
            return "end"
        return "pre_main"

    def check_main_page(self):
        self.click_x_y(72, 802)
        time.sleep(3)
        self.shot_screen()
        box = self.get_like_word_box('自动')
        if box:
            return True
        return False
