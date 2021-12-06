from script.base_script import BaseScript

#寻灵
class Xl(BaseScript):
    def start(self):
        self.click_x_y(953, 705)
        return 'do_task'

    def do_task(self):
        self.click_word('确定')
        self.click_word('开启寻灵任务')
        self.click_word('前往目标')
        self.click_word('使用')
        return 'do_task'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
task = Xl(config)
task.run()
