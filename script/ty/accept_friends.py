import time

from script.base_script import BaseScript


class AcceptFriends(BaseScript):
    def start(self):
        self.click_x_y(579, 990)
        return 'friend'

    def friend(self):
        box = self.get_like_word_box('添加好友')
        if box:
            self.click_box(box)
            return 'friends_apply'
        return 'friend'

    def friends_apply(self):
        box = self.get_like_word_box('好友申请')
        if box:
            self.click_box(box)
        time.sleep(2)
        box = self.get_like_word_box('全部接受')
        if box:
            self.click_box(box)
            return "end"
        return "friends_apply"
