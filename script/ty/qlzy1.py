from script.base_script import BaseScript
import time

#青林之野打６次
class Ql(BaseScript):
    def start(self):
        self.click_x_y(815, 673)
        return 'pre_task'

    def pre_task(self):
        self.click_word('开始挑战')
        self.click_word('确认选择')  # 该步骤是do_task留下的弹窗
        box = self.get_word_box('挂机')
        if box is None:
            return 'pre_task'
        time.sleep(2)
        box = self.get_like_word_box('自动战斗中')
        if box is None:
            self.click_word('挂机')
        self.walk_ahead(8)
        return 'do_task'

    def do_task(self):
        box = self.get_word_box('继续挑战')
        if box is not None:
            self.click_box(box)
            return 'pre_task'
        return 'do_task'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
task = Ql(config)
task.run()
