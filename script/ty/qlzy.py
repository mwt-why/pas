from script.base_script import BaseScript


#  青霖之野直接出
class QlZY(BaseScript):
    def start(self):
        self.click_x_y(815, 673)
        return 'tower'

    def tower(self):
        box = self.get_like_word_box('开始挑战')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('挂机')
        if box is not None:
            self.click_x_y(1856, 141)
        box = self.get_word_box('确定')
        if box is not None:
            self.click_box(box)
            return 'end'
        return 'tower'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
task = QlZY(config)
task.run()