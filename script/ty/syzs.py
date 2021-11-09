from script.base_script import BaseScript


class Sy(BaseScript):
    def start(self):
        self.click_x_y(1460, 900)
        return 'answer'

    def answer(self):
        box = self.get_word_box('A')
        if box is not None:
            self.click_box(box)
        box = self.get_word_box('B')
        if box is not None:
            self.click_box(box)
        box = self.get_word_box('C')
        if box is not None:
            self.click_box(box)
        box = self.get_word_box('D')
        if box is not None:
            self.click_box(box)
        return 'answer'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
task = Sy(config)
task.run()
