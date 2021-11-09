from script.base_script import BaseScript


class Xl(BaseScript):
    def start(self):
        self.click_x_y(953, 705)
        return 'team_up'

    def team_up(self):
        self.click_word('确定')
        return 'team_up'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
task = Xl(config)
task.run()
