from script.base_script import BaseScript
import time

package_name = 'com.netease.pm02'


class Start(BaseScript):
    def start(self):
        self.d.app_stop(package_name)
        time.sleep(3)
        self.d.app_start(package_name)
        return 'select_area'

    def select_area(self):
        area = self.task_data['area']
        box = self.get_word_box(area)
        if box is None:
            self.click_word('更换')
            pass
        return 'start_game'

    def start_game(self):
        time.sleep(5)
        box = self.get_like_word_box('公告')
        if box:
            self.click_x_y(1880, 89)
        box = self.get_word_box('开始游戏')
        if box:
            self.click_box(box)
            return 'pre_start'
        return 'start_game'

    def pre_start(self):
        self.click_word('开启云垂')
        box = self.get_word_box('今日不再弹出')
        self.click_word("稍后")
        if box:
            self.click_x_y(1985, 130)
        box = self.get_word_box('前去找回')
        if box:
            self.click_box(box)
            return 'click_comm_ft'
        box = self.get_word_box('我知道了')
        if box:
            self.click_box(box)
            return 'boon_hall'
        return 'pre_start'

    def click_comm_ft(self):
        box = self.get_like_word_box("签到")
        if box:
            self.click_box(box)
            self.click_x_y(1678, 230)
        box = self.get_word_box('普通找回')
        if box:
            self.click_box(box)
            return 'find_ret'
        return 'click_comm_ft'

    def find_ret(self):
        for i in range(10):
            time.sleep(2)
            self.click_word('花费')
        self.d.swipe_ext('up', box=(1359, 70, 1100, 1100))
        box = self.get_word_box('福利')
        if box:
            self.click_box(box)
            return 'get_boon'
        return 'find_ret'

    def get_boon(self):
        self.click_word('领取奖励')
        box = self.get_like_word_box("大厅")
        if box:
            self.click_box(box)
            return 'boon_hall'
        return 'get_boon'

    def boon_hall(self):
        box = self.get_like_word_box("签到")
        if box:
            self.click_box(box)
            self.click_x_y(1678, 230)
        result = self.check_main_page()
        if result:
            return 'end'
        return 'boon_hall'

    def check_main_page(self):
        self.click_x_y(72, 802)
        box = self.get_like_word_box('自动战斗中')
        if box:
            return True
        return False


config = {'id': '0', 'ip': '192.168.31.92', 'role_name': '一世忆南',
          'task': 'rc', 'area': '长歌行', 'type': '1', 'mac': 'xd1', 'serial': '936X1XHD9'}
start = Start(config)
start.run()
