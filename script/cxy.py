# 出学院
import time
from script.base_script import BaseScript

package_name = 'com.netease.pm02'
close_map = {'新服开启公告': [1880, 85],
             '今日不再弹出': [1980, 128],
             '疾速修行秘卷': [1660, 300],
             '己签': [1685, 280],
             }
close_list = ['领取', '签到', '使用']
all_need_close = ['新服开启公告', '今日不再弹出', '疾速修行秘卷', '己签', '领取', '签到', '使用']
task_index_list = [1, 3, 4]
task_map = {'must_do': 0, 'demon': 0, 'fight': 0, 'casual': 0}
key_dict = {'click_daily': 0, 'click_wsw': 0}
menu_button = (1746, 63)


class CXY(BaseScript):

    def start(self):
        self.d.app_stop(package_name)
        time.sleep(3)
        self.d.app_start(package_name)
        return 'start_game'

    def start_game(self):
        box = self.get_word_box('公告')
        if box is not None:
            pass
        box = self.get_word_box('开始游戏')
        if box is not None:
            self.click_box(box)
            return 'boot_yc'
        return 'start_game'

    def boot_yc(self):
        box = self.get_word_box('开启云垂')
        if box is not None:
            self.click_box(box)
        state = self.close_modal(close_map, close_list)
        if state == 1:
            return 'prepare'
        return 'boot_yc'

    def prepare(self):
        result = self.contain_words(all_need_close)
        if result is not None:
            return 'boot_yc'
        return 'rc'

    def rc(self):
        self.click_word_list(('日程', '目程', '圄程'))
        if self.get_word_box('全部活动') is None:
            return 'prepare'
        for k in task_map.keys():
            if task_map[k] == 0:
                print('进入' + k + '方法')
                return k

    def must_do(self):
        time.sleep(2)
        self.click_word('必做')
        if len(task_index_list) == 0:
            task_map['must_do'] = 1
            return 'rc'
        task_index = task_index_list.pop()
        if task_index == 1:
            return self.join_by_coo(420, 437, 'wsw')
        elif task_index == 3:
            return self.join(task_index, '寻灵', 'xl')
        return 'must_do'

    def join_by_coo(self, x, y, ret):
        self.click_x_y(x, y)
        return ret

    def join(self, task_index, ref, ret):
        box = self.get_refX_box('参加', ref, 50)
        if box is not None:
            self.click_box(box)
            return ret
        task_index_list.append(task_index)
        return 'rc'

    # 万事屋
    def wsw(self):
        if key_dict['click_daily'] == 0:
            box = self.get_word_box('日常')
            if box is not None:
                self.click_box(box)
                key_dict['click_daily'] = 1
        if key_dict['click_wsw'] == 0:
            box = self.get_like_word_box('万事屋(')
            if box is not None:
                self.click_box(box)
                key_dict['click_wsw'] = 1
        self.click_word('跳过')
        box = self.get_word_box('回去告诉无忌宝箱放好了')
        if box is not None:
            self.click_box(box)
        box = self.get_word_box('使用')
        if box is not None:
            self.click_box(box)
            return 'exit_wsw'
        return 'wsw'

    def exit_wsw(self):
        self.click_x_y(menu_button[0], menu_button[1])
        return 'must_do'

    # 寻灵
    def xl(self):
        self.click_word('确定')
        time.sleep(2)
        box = self.get_word_box('创建队伍')
        if box is not None:
            self.click_box(box)
            return 'go_xl'
        return 'xl'

    def go_xl(self):
        self.click_word('前往目标')
        time.sleep(5)
        self.click_word('开启寻灵任务')
        self.click_word('使用')
        self.click_word('装备')
        box = self.get_like_word_box('5次寻灵任务已完成')
        if box is not None:
            self.click_word('确定')
            self.click_x_y(menu_button[0], menu_button[1])
            self.click_word_list(('日程', '目程'))
            if self.get_word_box('全部活动') is None:
                return 'must_do'
        return 'go_xl'

    def fb(self):
        self.click_word('进入副本')
        self.click_word('普通')
        self.click_word('组队')
        self.click_word('创建队伍')
        box = self.get_word_box('前往目标')
        if box is not None:
            self.click_box(box)
            return 'pre_fb'
        return 'fb'

    def pre_fb(self):
        self.click_word('普通')
        self.click_word('灵墟')
        box = self.get_word_box('前往副本')
        if box is not None:
            self.click_box(box)
            return 'fb_doing'
        return 'pre_fb'

    def fb_doing(self):
        self.click_word('确定')
        self.click_word('确定')
        self.click_word('跳过')
        self.click_word('继续挑战')
        return 'fb_doing'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc'}
cxy = CXY(config)
cxy.run()
