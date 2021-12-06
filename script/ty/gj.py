from script.base_script import BaseScript

#工会任务
class Gj(BaseScript):
    def start(self):
        self.click_x_y(1687, 950)
        return 'notice'

    def notice(self):
        box = self.get_word_box('接受任务')
        if box is not None:
            self.click_box(box)
            return 'do_task'
        return 'notice'

    def do_task(self):
        self.click_word('跳过')
        self.click_word('使用')
        return 'do_task'


config = {'id': '0', 'ip': '192.168.43.65', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
task = Gj(config)
task.run()
