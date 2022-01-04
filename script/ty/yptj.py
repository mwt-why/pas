from script.base_script import BaseScript
import time


#  装备药品
class YPTJ(BaseScript):

    def start(self):
        self.click_x_y(1978, 330)
        return 'drug'

    def drug(self):
        box = self.get_like_word_box('药品')
        if box is not None:
            self.click_box(box)
            return 'go_buy'
        return 'drug'

    def go_buy(self):
        box = self.get_like_word_box('键添加')
        if box is not None:
            self.click_x_y(413, 462)
            return 'to_buy'
        return 'go_buy'

    def go_buy1(self):
        box = self.get_like_word_box('键添加')
        if box is not None:
            self.click_x_y(413, 770)
            return 'to_buy1'
        return 'go_buy1'

    def add(self):
        box = self.get_like_word_box('键添加')
        if box is not None:
            self.click_box(box)
            return 'buy'
        return 'add'

    def to_buy(self):
        box = self.get_like_word_box('晨露饮')
        if box is not None:
            self.click_box(box)
            return 'go_buy1'
        box = self.get_like_word_box('商会商店')
        if box is not None:
            self.click_box(box)
            return 'buy'
        return 'to_buy'

    def to_buy1(self):
        box = self.get_like_word_box('星茸花糕')
        if box is not None:
            self.click_box(box)
            return 'exit'
        box = self.get_like_word_box('商会商店')
        if box is not None:
            self.click_box(box)
            return 'buy'
        return 'to_buy1'

    def buy(self):
        box = self.get_like_word_box('购买')
        if box is not None:
            self.click_x_y(1753, 659)
            return 'big'
        return 'buy'

    def big(self):
        box = self.get_like_word_box('最大')
        if box is not None:
            self.click_box(box)
            box = self.get_like_word_box('确定')
            if box is not None:
                self.click_box(box)
                box = self.get_word_box('购买')
                if box is not None:
                    self.click_box(box)
                    self.click_x_y(100, 76)
                    return 'go_buy1'
        return 'big'

    def exit(self):
        box = self.get_like_word_box('仓库')
        if box is not None:
            self.click_x_y(100, 76)
            return 'end'
        return 'exit'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行', 'type': '1',
          'mac': 'fdsafa'}
start = YPTJ(config)
start.run()
