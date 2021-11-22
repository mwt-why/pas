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
        box = self.get_word_box('开始游戏')
        if box is not None:
            self.click_box(box)
            return 'pre_start'
        return 'start_game'

    def pre_start(self):
        self.click_word('开启云垂')
        box = self.get_word_box('今日不再弹出')
        if box is not None:
            self.click_x_y(1985, 130)
        box = self.get_word_box('前去找回')
        if box is not None:
            self.click_box(box)
            return 'click_comm_ft'
        box = self.get_word_box('我知道了')
        if box is not None:
            self.click_box(box)
            return 'boon_hall'
        return 'pre_start'

    def click_comm_ft(self):
        box = self.get_word_box('普通找回')
        if box is not None:
            self.click_box(box)
            return 'find_ret'
        return 'click_comm_ft'

    def find_ret(self):
        for i in range(4):
            time.sleep(2)
            self.click_word('花费')
        self.d.swipe_ext('up', box=(1359, 70, 1100, 1100))
        box = self.get_word_box('福利')
        if box is not None:
            self.click_box(box)
            return 'get_boon'
        return 'find_ret'

    def get_boon(self):
        self.click_word('领取奖励')
        box = self.get_word_box('福利太厅')
        if box is not None:
            self.click_box(box)
            return 'boon_hall'
        return 'get_boon'

    def boon_hall(self):
        role_name = self.task_data['role_name']
        box = self.get_word_box(role_name)
        if box is not None:
            return 'end'
        self.walk_ahead(1)
        return 'boon_hall'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
start = Start(config)
start.run()
