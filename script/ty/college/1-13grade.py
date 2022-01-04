import time

from script.base_script import BaseScript


# 升级到16
class Grade(BaseScript):
    # 最开始
    @staticmethod
    def start():
        return 'window_wait'

    # 窗口等待
    def window_wait(self):
        box = self.get_like_word_box('窗边等待')
        if box is not None:
            self.click_box(box)
            return 'answer_no_worry'
        return 'window_wait'

    # 回答要不要紧
    def answer_no_worry(self):
        box = self.get_like_word_box('相识的梦')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip2'
        return 'answer_no_worry'

    # 跳过回答
    def jump_over_tip2(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            # 需要等待一会
            return 'comfirm_name'
        return 'jump_over_tip2'
        # 任务追踪栏引导

    # 确认姓名
    def comfirm_name(self):
        box = self.get_like_word_box('确认姓名')
        if box is not None:
            self.click_box(box)
            return 'comfirm_name2'
        return 'comfirm_name'

    # 确认姓名2
    def comfirm_name2(self):
        box = self.get_like_word_box('确认姓名')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip3'
        return 'comfirm_name2'

    # 跳过回答
    def jump_over_tip3(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'closet'
        return 'jump_over_tip3'

    # 衣柜
    def closet(self):
        box = self.get_like_word_box('衣柜')
        if box is not None:
            self.click_box(box)
            return 'choose_white'
        return 'closet'

    # 选白衣服
    def choose_white(self):
        box = self.get_like_word_box('白色制服')
        if box is not None:
            self.click_box(box)
            return 'comfirm_white'
        return 'choose_white'

    # 决定是你了
    def comfirm_white(self):
        box = self.get_like_word_box('决定是你了')
        if box is not None:
            self.click_box(box)
            return 'equip'
        return 'comfirm_white'

    def equip(self):
        box = self.get_like_word_box('装备')
        if box is not None:
            self.click_box(box)
            self.click_word('装备')
            return 'tianyu_photo'
        return 'equip'

    #     天谕岛相册
    def tianyu_photo(self):
        box = self.get_like_word_box('相册')
        if box is not None:
            self.click_box(box)
            return 'getout_home'
        return 'tianyu_photo'

    # 离开房间
    def getout_home(self):
        self.click_word('完成')
        box = self.get_like_word_box('离开房间')
        if box is not None:
            self.click_box(box)
            return 'in_lobby'
        return 'getout_home'

    # 人聚集在大厅
    def in_lobby(self):
        box = self.get_like_word_box('聚集在大厅')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip4'
        return 'in_lobby'

    # 跳过回答
    def jump_over_tip4(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('哎')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip5'
        return 'jump_over_tip4'

    # 跳过
    def jump_over_tip5(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            self.click_word('跳过')
            return 'fight_model'
        return 'jump_over_tip5'

    # 前往甲板
    def fight_model(self):
        box = self.get_like_word_box('确认')
        if box:
            self.click_box(box)
            self.click_word('确认')
            return 'go_deck'
        return 'fight_model'

        # 前往甲板

    def go_deck(self):
        box = self.get_like_word_box('前往甲板')
        if box is not None:
            return 'sing_kick'
        return 'go_deck'

    def sing_kick(self):
        box = self.get_like_word_box('菜单')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('游记')
        if box is not None:
            self.click_box(box)
            return 'task'
        return 'sing_kick'

    def task(self):
        box = self.get_like_word_box('返回')
        if box is not None:
            self.click_x_y(490, 450)
            return 'task_go'
        return 'task'

    def task_go(self):
        box = self.get_like_word_box('跳过本章')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('确定')
        if box:
            self.click_box(box)
            return 'equip1'
        return 'task_go'

    def equip1(self):
        box = self.get_like_word_box('装备')
        if box is not None:
            self.click_box(box)
            self.click_word('装备')
            self.click_word('装备')
            self.click_word('装备')
            self.click_word('使用')
            self.click_word('使用')
            self.click_word('阿笑')
            return 'go_to_return'
        return 'equip1'

    def go_to_return(self):
        box = self.get_like_word_box('空白处关闭')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('返回')
        if box is not None:
            self.click_box(box)
            return 'open_cloud_and_sea'
        return 'go_to_return'

    #     开区云与海
    def open_cloud_and_sea(self):
        box = self.get_like_word_box('云与海')
        if box is not None:
            self.click_box(box)
            return 'cloud_and_sea'
        return 'open_cloud_and_sea'

    def cloud_and_sea(self):
        box = self.get_like_word_box('开启')
        if box is not None:
            self.click_box(box)
            return 'see_yuan'
        return 'cloud_and_sea'

    # 见到元裘了么
    def see_yuan(self):
        box = self.get_like_word_box('见到元裘')
        self.click_like_word('云与海')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('工牌')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('没问题')
        if box:
            self.click_box(box)
            return 'cloud_and_sea2'
        return 'see_yuan'

    def cloud_and_sea2(self):
        box = self.get_like_word_box('我很喜欢啊')
        self.click_like_word('云与海')
        if box is not None:
            self.click_box(box)
            return 'cloud_and_sea3'
        return 'cloud_and_sea2'

    def cloud_and_sea3(self):
        box = self.get_like_word_box('那好')
        self.click_like_word('云与海')
        if box is not None:
            self.click_box(box)
            return 'self_cook'
        return 'cloud_and_sea3'

        # 自由创作
        # TODO 需要点击图片

    def self_cook(self):
        box = self.get_like_word_box('烹饪')
        self.click_like_word('云与海')
        # self.click_like_word('跳过')
        # self.click_like_word('确认')
        if box is not None:
            self.click_x_y(1790, 355)
            self.click_x_y(350, 265)
            self.click_x_y(500, 260)
            self.click_x_y(190, 410)
            self.click_x_y(500, 385)
            self.click_x_y(350, 385)
        box = self.get_like_word_box('成功率100%')
        if box:
            self.click_word('烹饪')
            return 'cloud_and_sea4'
        return 'self_cook'

    def cloud_and_sea4(self):
        box = self.get_like_word_box('协会的竞争')
        self.click_like_word('云与海')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('流星')
        self.click_like_word('跳过')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('听上去')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('那我就')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('完成')
        if box:
            self.click_box(box)
            return 'cloud_and_sea5'
        return 'cloud_and_sea4'

    def cloud_and_sea5(self):
        box = self.get_like_word_box('在天上')
        self.click_like_word('云与海')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('前所未见')
        self.click_like_word('跳过')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('但我还有')
        self.click_like_word('跳过')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('你究竟是谁')
        self.click_like_word('跳过')
        if box:
            self.click_box(box)
            return 'cloud_and_sea6'
        return 'cloud_and_sea5'

    def cloud_and_sea6(self):
        box = self.get_like_word_box('工牌已经不见')
        self.click_like_word('云与海')
        self.click_like_word('跳过')
        if box:
            self.click_box(box)
            self.click_like_word('完成')
            return 'cloud_and_sea7'
        return 'cloud_and_sea6'

    def cloud_and_sea7(self):
        box = self.get_like_word_box('凌空之')
        self.click_like_word('云与海')
        self.click_like_word('使用')
        if box:
            self.click_box(box)
            return 'the_sky_wind'
        return 'cloud_and_sea7'

    def the_sky_wind(self):
        box = self.get_like_word_box('可以点击')
        self.click_like_word('跳过')
        if box:
            self.click_x_y(2079, 635)
        box = self.get_like_word_box('点击这里')
        if box:
            self.click_x_y(1916, 800)
            self.click_like_word('凌空之')
            return 'the_sky_wind1'
        return 'the_sky_wind'

    def the_sky_wind1(self):
        box = self.get_like_word_box('凌空之')
        self.click_like_word('跳过')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('点了点头')
        if box:
            self.click_box(box)
            return 'the_sky_wind2'
        return 'the_sky_wind1'

    def the_sky_wind2(self):
        box = self.get_like_word_box('雪夜芳华')
        self.click_like_word('跳过')
        if box:
            self.click_box(box)
            self.click_word('领取')
            return 'the_sky_wind3'
        return 'the_sky_wind2'

    def the_sky_wind3(self):
        box = self.get_like_word_box('来自师姐的问候')
        self.click_like_word('跳过')
        if box:
            self.click_box(box)
            return 'finish_15_step'
        return 'the_sky_wind3'

    def finish_15_step(self):
        box = self.get_like_word_box('接下来学习')
        self.click_like_word('来自师姐的问候')
        if box:
            self.click_box(box)
            return 'finish_15_step1'
        return 'finish_15_step'

    def finish_15_step1(self):
        box = self.get_like_word_box('师姐的馈赠')
        self.click_like_word('来自师姐的问候')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('借我点')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('师姐的考验')
        if box:
            self.click_box(box)
            return 'college_main_thing'
        return 'finish_15_step1'

        # 学院课程

    def college_main_thing(self):
        box = self.get_like_word_box('学院课程')
        self.click_like_word('跳过')
        if box is not None:
            self.click_box(box)
            return 'say_why'
        return 'college_main_thing'

    def say_why(self):
        box = self.get_like_word_box('为什么')
        self.click_like_word('跳过')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('交给我吧')
        self.click_like_word('跳过')
        if box is not None:
            self.click_box(box)
            return 'give_them_to_me'
        return 'say_why'

    def give_them_to_me(self):
        box = self.get_like_word_box('白露递来一本书册')
        self.click_like_word('跟随白露')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('这是什么')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('学院教材')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('哪个等级的')
        if box:
            self.click_box(box)
        box = self.get_like_word_box('端木前辈')
        if box:
            self.click_box(box)
            return 'listen_is_difficult'
        return 'give_them_to_me'

    def listen_is_difficult(self):
        box = self.get_like_word_box('听上去好难')
        self.click_like_word('跳过')
        if box is not None:
            self.click_box(box)
            return 'work_hard'
        return 'listen_is_difficult'

    def work_hard(self):
        box = self.get_like_word_box('我会努力的')
        if box is not None:
            self.click_box(box)
            return 'listen_yang_class'
        return 'work_hard'

    def listen_yang_class(self):
        box = self.get_like_word_box('介绍学院课程')
        if box is not None:
            self.click_box(box)
            return 'bai_give_to_me'
        return 'listen_yang_class'

    def bai_give_to_me(self):
        box = self.get_like_word_box('白露姐给')
        self.click_like_word('跳过')
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('云垂学院')
        self.click_like_word('跳过')
        if box is not None:
            return 'end'
        return 'bai_give_to_me'


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行', 'type': '1',
          'mac': 'fdsafa'}
fb = Grade(config)
fb.run()
