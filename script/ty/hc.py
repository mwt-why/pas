from script.base_script import BaseScript


#  回城
class HC(BaseScript):
    @staticmethod
    def start():
        return 'back'

    def back(self):
        box = self.get_like_word_box('提升战力')
        if box is not None:
            self.click_x_y(1999, 190)
        box = self.get_like_word_box('世界地图')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('苏澜郡')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('苏澜郡')
        if box is not None:
            self.click_x_y(885, 610)
            return 'end'
        return 'back'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行', 'type': '1',
          'mac': 'fdsafa'}
start = HC(config)
start.run()
