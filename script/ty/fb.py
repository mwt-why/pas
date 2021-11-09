from script.base_script import BaseScript


class Fb(BaseScript):
    def start(self):
        box = self.get_word_box('副本')
        if box is not None:
            self.click_box(box)
            return 'team_up'
        return 'start'

    def team_up(self):
        self.click_word('普通')
        self.click_word('组队')
        self.click_word('创建团队')
        box = self.get_word_box('前往目标')
        if box is not None:
            self.click_box(box)
            return 'select_model'
        return 'team_up'

    def select_model(self):
        self.click_word('普通')
        self.click_word('灵墟')
        box = self.get_word_box('前往副本')
        if box is not None:
            self.click_box(box)
            return 'fb_doing'
        return 'select_model'

    def fb_doing(self):
        self.click_word('跳过')
        if self.get_word_box('继续挑战') is not None and self.get_word_box('关闭'):
            self.click_word('关闭')
            return 'over_fb'
        return 'fb_doing'

    def over_fb(self):
        return 'end'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
fb = Fb(config)
fb.run()
