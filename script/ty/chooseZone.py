from script.base_script import BaseScript


# 登录注册账号
class Zc(BaseScript):
    def start(self):
        return 'click_change'

    # 判断是不是有三个长歌行账号，没有就创建
    def click_change(self):
        box = self.get_like_word_box('更换')
        if box is not None:
            self.click_box(box)
            return 'choose_cgx'

    def choose_cgx(self):
        count = self.count_word('忆江南')
        if count == 3:
            return 'end'
        else:
            return 'choose_guanFang1qu'

    # 没有长歌行账号，重新创建
    def choose_guanFang1qu(self):
        self.click_word('官方1区')
        # box = self.get_like_word_box('长歌行')
        box = self.get_like_word_box('忆江南')
        if box is not None:
            self.click_box(box)
            return 'create_character'
        return 'choose_guanFang1qu'

    # 首页进入游戏界面
    def create_character(self):
        # self.click_word('长歌行')
        self.click_word('忆江南')
        # 直接按坐标点击
        self.click_x_y(self,1160,900)
        return 'add_character'

        # box = self.get_like_word_box('开始游戏')
        # if box is not None:
        #     self.click_word('开始游戏')
        #     return 'add_character'
        # return 'create_character'
    # todo 需要判断有多少个创建角色,三个的按钮位置不一样
    #     没有创建角色文字，直接退出
    #     todo，需要确定点击第一个创建角色
    def add_character(self):
        count = self.count_word(self, "创建角色")
        if count == 0:
            return 'end'
        else:
            box = self.get_like_word_box('创建角色')
            if box is not None:
                self.click_box(box)
                return 'choose_sex'
            return 'end'

    # 选取角色 玉虚
    def choose_sex(self):
        self.click_word('下一步')
        box = self.get_like_word_box('下一步')
        if box is not None:
            self.click_word('下一步')
        else:
            return 'choose_sex'
        box = self.get_like_word_box('开启云垂')
        if box is not None:
            self.click_word('开启云垂')
            return 'choose_name'
        else:
            return 'choose_sex'

    #获取随机名字
    def choose_name(self):
        box = self.get_like_word_box('确定')
        if box is not None:
            self.click_x_y(self, 1160, 580)
            self.click_word('确定')
            return 'end'
        else:
            return 'choose_name'



config = {'id': '0', 'ip': '192.168.43.122', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行', 'type': '1',
          'mac': 'fdsafa', 'serial': '5b7fb6e3'}
fb = Zc(config)
fb.run()
