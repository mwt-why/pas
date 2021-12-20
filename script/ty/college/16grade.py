from script.base_script import BaseScript

# 升级到16
class Grade(BaseScript):
    # 最开始
    def start(self):
        box = self.get_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip1'
        return 'start'

# 任务追踪栏引导
    def jump_over_tip1(self):
        box = self.get_like_word_box('任务追踪引导')
        if box is not None:
            self.click_word('确定')
            return 'window_wait'
        return 'jump_over_tip1'

    # 窗口等待
    def window_wait(self):
        box = self.get_like_word_box('窗边等待')
        if box is not None:
            self.click_box(box)
            return 'answer_no_worry'
        return 'window_wait'

    #回答要不要紧
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
            self.click_word('跳过')
            # 需要等待一会
            self.click_word('跳过')
            return 'comfirm_name'
        return 'jump_over_tip2'

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
            self.click_word('跳过')
            return 'comfirm_jump_over_tip3'
        return 'jump_over_tip3'

    # 任务追踪栏引导
    def comfirm_jump_over_tip3(self):
        box = self.get_like_word_box('任务追踪引导')
        if box is not None:
            self.click_word('确定')
            return 'closet'
        return 'comfirm_jump_over_tip3'

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
            self.click_like_word("装备")
            self.click_like_word("相册")
            return 'tianyu_photo'
        return 'comfirm_white'

#     天谕岛相册
    def tianyu_photo(self):
        box = self.get_like_word_box('完成')
        if box is not None:
            self.click_box(box)
            return 'choose_white'
        return 'tianyu_photo'

# 离开房间
    def getout_home(self):
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
            self.click_word('跳过')
            self.click_like_word('协会')
            return 'jump_over_tip5'
        return 'jump_over_tip4'

    # 跳过
    def jump_over_tip5(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_word('跳过')
            return 'fight_model'
        return 'jump_over_tip5'

    # 确认作战模式，2个确认
    def fight_model(self):
        box = self.get_like_word_box('确认')
        if box is None:
            self.click_word('确认')
            return 'go_deck'
        return 'fight_model'

    # 前往甲板
    def go_deck(self):
        box = self.get_like_word_box('前往甲板')
        if box is not None:
            self.click_box(box)
            return 'sing_kick'
        return 'go_deck'

    # 单攻
    def sing_kick(self):
        box = self.get_like_word_box('单攻')
        if box is not None:
            self.click_box(box)
            return 'stop_war'
        return 'sing_kick'

    # 阻止打架
    def stop_war(self):
        box = self.get_like_word_box('制止')
        self.click_like_word('单攻')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip6'
        return 'stop_war'

    # 跳过
    def jump_over_tip6(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_word('跳过')
            return 'talk_nan'
        return 'jump_over_tip6'

    # 南歌对话
    def talk_nan(self):
        box = self.get_like_word_box('南歌对话')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip7'
        return 'talk_nan'

    # 跳过
    def jump_over_tip7(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_word('跳过')
            self.click_like_word("大赢所有")
            return 'jump_over_tip8'
        return 'jump_over_tip7'

    # 跳过
    def jump_over_tip8(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_word('跳过')
            return 'jump_over_imp_tip'
        return 'jump_over_tip8'

    # 跳过重要剧情
    def jump_over_imp_tip(self):
        box = self.get_like_word_box('跳过重要剧情')
        if box is not None:
            self.click_like_word('跳过重要剧情')
            self.click_like_word('残忍跳过')
            return 'say_bey_with_nan'
        return 'jump_over_imp_tip'

# 与南歌告别
    def say_bey_with_nan(self):
        box = self.get_like_word_box('夏颜道别')
        if box is not None:
            self.click_box(box)
            self.click_like_word("跳过")
            return 'go_to_jinbake'
        return 'say_bey_with_nan'

# 鲸巴客
    def go_to_jinbake(self):
        box = self.get_like_word_box('鲸巴客')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip9'
        return 'go_to_jinbake'

    # 跳过
    def jump_over_tip9(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'jump_over_main_line'
        return 'jump_over_tip9'

    # 跳过该章节主线
    def jump_over_main_line(self):
        box = self.get_like_word_box('跳过该')
        if box is not None:
            self.click_word("确定")
            return 'click_white_to_jump'
        return 'jump_over_main_line'

# 点击空白处关闭
    def click_white_to_jump(self):
        box = self.get_like_word_box('空白处关闭')
        if box is not None:
            self.click_box(box)
            return 'equip_on'
        return 'click_white_to_jump'

# 装备
    def equip_on(self):
        box = self.get_like_word_box('装备')
        self.click_like_word("装备")
        if box is None:
            self.click_box(box)
            return 'to_use'
        return 'equip_on'

    # 使用
    def to_use(self):
        box = self.get_like_word_box('使用')
        self.click_like_word("使用")
        if box is None:
            self.click_box(box)
            return 'open_cloud_and_sea'
        return 'to_use'

#     开区云与海
    def open_cloud_and_sea(self):
        box = self.get_like_word_box('开启')
        if box is None:
            self.click_box(box)
            return 'cloud_and_sea'
        return 'open_cloud_and_sea'

# 云与海的故事
    def cloud_and_sea(self):
        box = self.get_like_word_box('云与海')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip10'
        return 'cloud_and_sea'

    # 跳过
    def jump_over_tip10(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'jump_over_main_line'
        return 'jump_over_tip10'

# 云与海的故事
    def cloud_and_sea2(self):
        box = self.get_like_word_box('云与海')
        self.click_like_word("云与海")
        if box is None:
            # self.click_box(box)
            return 'see_yuan'
        return 'cloud_and_sea2'

# 见到元裘了么
    def see_yuan(self):
        box = self.get_like_word_box('见到元裘')
        if box is not None:
            self.click_box(box)
            self.click_like_word("工牌")
            self.click_like_word("没问题")

            return 'cloud_and_sea3'
        return 'see_yuan'

# 云与海的故事
    def cloud_and_sea3(self):
        box = self.get_like_word_box('云与海')
        self.click_like_word("云与海")
        if box is None:
            # self.click_box(box)
            return 'jump_over_tip11'
        return 'cloud_and_sea3'

    # 跳过
    def jump_over_tip11(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'i_so_in_love'
        return 'jump_over_tip11'

    # 我很喜欢
    def i_so_in_love(self):
        box = self.get_like_word_box('我很喜欢')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip12'
        return 'i_so_in_love'

    # 跳过
    def jump_over_tip12(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'cloud_and_sea4'
        return 'jump_over_tip12'

# 云与海的故事
    def cloud_and_sea4(self):
        box = self.get_like_word_box('云与海')
        self.click_like_word("云与海")
        if box is None:
            # self.click_box(box)
            return 'jump_over_tip13'
        return 'cloud_and_sea4'

    # 跳过
    def jump_over_tip13(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'cloud_and_sea4'
        return 'jump_over_tip13'

    # 帮忙准备
    def jump_over_tip13(self):
        box = self.get_like_word_box('帮忙准备')
        if box is not None:
            self.click_box(box)
            return 'cloud_and_sea4'
        return 'jump_over_tip13'

# 云与海的故事
    def cloud_and_sea5(self):
        box = self.get_like_word_box('云与海')
        self.click_like_word("云与海")
        if box is None:
            # self.click_box(box)
            return 'jump_over_tip13'
        return 'cloud_and_sea5'

    # 自由创作
    # TODO 需要点击图片
    def self_cook(self):
        box = self.get_like_word_box('烹饪')
        if box is not None:
            self.click_x_y(self, 1790, 355)
            self.click_x_y(self, 350, 265)
            self.click_x_y(self, 500, 260)
            self.click_x_y(self, 190, 410)
            self.click_x_y(self, 500, 385)
            self.click_box(box)
            return 'cloud_and_sea6'
        return 'self_cook'

    # 云与海的故事
    def cloud_and_sea6(self):
        box = self.get_like_word_box('云与海')
        self.click_like_word("云与海")
        if box is None:
            # self.click_box(box)
            return 'jump_over_tip14'
        return 'cloud_and_sea6'

    # 跳过
    def jump_over_tip14(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'comp_organize'
        return 'jump_over_tip14'

    # 竞争组织
    def comp_organize(self):
        box = self.get_like_word_box('竞争组织')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip15'
        return 'comp_organize'

    # 跳过
    def jump_over_tip15(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'liu_xing'
        return 'jump_over_tip15'

    # 流星
    def liu_xing(self):
        box = self.get_like_word_box('流星')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip16'
        return 'liu_xing'

    # 跳过
    def jump_over_tip16(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'chage_loop'
        return 'jump_over_tip16'

    # 改变星轨
    def chage_loop(self):
        box = self.get_like_word_box('改变星轨')
        if box is not None:
            self.click_box(box)
            return 'realy_can'
        return 'chage_loop'

    # 真的可以？
    def realy_can(self):
        box = self.get_like_word_box('真的可以')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip16'
        return 'realy_can'


    # TODO
    # 需要画画
    def has_done(self):
        box = self.get_like_word_box('完成')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip16'
        return 'has_done'

    # 云与海的故事
    def cloud_and_sea7(self):
        box = self.get_like_word_box('云与海')
        self.click_like_word("云与海")
        if box is None:
            # self.click_box(box)
            return 'sky_fish'
        return 'cloud_and_sea7'

# 天上烤鱼
    def sky_fish(self):
        box = self.get_like_word_box('天上烤鱼')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip17'
        return 'sky_fish'

    # 跳过
    def jump_over_tip17(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'like_simple_life'
        return 'jump_over_tip17'

# 想要闲适生活
    def like_simple_life(self):
        box = self.get_like_word_box('想要闲适')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip18'
        return 'like_simple_life'

    # 跳过
    def jump_over_tip18(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'more_que'
        return 'jump_over_tip18'

    # 还有一个问题
    def more_que(self):
        box = self.get_like_word_box('还有一个问题')
        if box is not None:
            self.click_box(box)
            return 'can_we_see_again'
        return 'more_que'

    # 还能再见
    def can_we_see_again(self):
        box = self.get_like_word_box('还能再见')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip19'
        return 'can_we_see_again'

    # 跳过
    def jump_over_tip19(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'cloud_and_sea8'
        return 'jump_over_tip19'

    # 云与海的故事
    def cloud_and_sea8(self):
        box = self.get_like_word_box('云与海')
        self.click_like_word("云与海")
        if box is None:
            # self.click_box(box)
            return 'jump_over_tip20'
        return 'cloud_and_sea8'

    # 跳过
    def jump_over_tip20(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'cloud_and_sea9'
        return 'jump_over_tip20'

    # 云与海的故事
    def cloud_and_sea9(self):
        box = self.get_like_word_box('云与海')
        self.click_like_word("云与海")
        if box is None:
            # self.click_box(box)
            return 'has_done2'
        return 'cloud_and_sea9'

# 完成
    def has_done2(self):
        box = self.get_like_word_box('完成')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip21'
        return 'has_done2'

    # 跳过
    def jump_over_tip21(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'cloud_and_sea10'
        return 'jump_over_tip21'

    # 云与海的故事
    def cloud_and_sea10(self):
        box = self.get_like_word_box('云与海')
        self.click_like_word("云与海")
        if box is None:
            # self.click_box(box)
            return 'some_thing_to_use'
        return 'cloud_and_sea10'

# 使用
    def some_thing_to_use(self):
        box = self.get_like_word_box('使用')
        self.click_like_word("使用")
        if box is None:
            # self.click_box(box)
            return 'the_sky_wind'
        return 'some_thing_to_use'

    # 凌空之翼
    def the_sky_wind(self):
        box = self.get_like_word_box('凌空之翼')
        if box is None:
            self.click_box(box)
            return 'jump_over_tip22'
        return 'the_sky_wind'

    # 跳过
    def jump_over_tip22(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            self.click_x_y(self,2117,630)
            return 'the_sky_wind3'
        return 'jump_over_tip22'

# 完成引导任务
    def the_sky_wind3(self):
        box = self.get_like_word_box('凌空之翼')
        self.click_like_word('凌空之翼')
        if box is None:
            # self.click_box(box)
            # 点击关闭
            self.click_x_y(self,2130,190)
            return 'the_sky_wind4'
        return 'the_sky_wind3'

    # 凌空之翼
    def the_sky_wind4(self):
        box = self.get_like_word_box('凌空之翼')
        if box is not None:
            self.click_box(box)
            self.click_like_word("跳过")
            self.click_like_word("领取")
            self.click_like_word("跳过")
            return 'finish_15_step'
        return 'the_sky_wind4'

    # 来自师姐的问候
    def finish_15_step(self):
        box = self.get_like_word_box('师姐的问候')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip23'
        return 'finish_15_step'

# 跳过
    def jump_over_tip23(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'sister_question'
        return 'jump_over_tip23'

    # 来自师姐的问候
    def sister_question(self):
        box = self.get_like_word_box('师姐的问候')
        if box is not None:
            self.click_box(box)
            self.click_like_word("跳过")
            self.click_like_word("装备")
            self.click_like_word("使用")
            # 返回
            self.click_x_y(self,180,66)
            self.click_like_word("完成")
            self.click_like_word("跳过")
            return 'nothing_to_sister'
        return 'sister_question'

# 不麻烦师姐
    def nothing_to_sister(self):
        box = self.get_like_word_box('麻烦师姐')
        if box is not None:
            self.click_box(box)
            self.click_like_word("跳过")
            self.click_like_word("完成")
            self.click_like_word("跳过")
            return 'college_main_thing'
        return 'nothing_to_sister'

  # 学院课程
    def college_main_thing(self):
        box = self.get_like_word_box('学院课程')
        if box is not None:
            self.click_box(box)
            return 'jump_over_tip24'
        return 'college_main_thing'

# 跳过
    def jump_over_tip24(self):
        box = self.get_like_word_box('跳过')
        if box is not None:
            self.click_box(box)
            return 'say_why'
        return 'jump_over_tip24'

    def say_why(self):
        box = self.get_like_word_box('为什么')
        if box is not None:
            self.click_box(box)
            self.click_like_word("跳过")
            return 'give_them_to_me'
        return 'say_why'

# 交给我吧
    def give_them_to_me(self):
        box = self.get_like_word_box('交给我吧')
        if box is not None:
            self.click_box(box)
            return 'follow_bai'
        return 'give_them_to_me'

    # 跟随白露
    def follow_bai(self):
        box = self.get_like_word_box('跟随白露')
        if box is not None:
            self.click_box(box)
            return 'school_class'
        return 'follow_bai'

    # 学院课程
    def school_class(self):
        box = self.get_like_word_box('学院课程')
        self.click_like_word('学院课程')
        if box is None:
            self.click_like_word("这是什么")
            self.click_like_word("学院教材")
            self.click_like_word("跳过")

            return 'bai_high_lvl'
        return 'school_class'

    # 白姐等级高
    def bai_high_lvl(self):
        box = self.get_like_word_box('等级一定很高')
        if box is not None:
            self.click_box(box)
            return 'duanmu_high_lvl'
        return 'bai_high_lvl'

    # 端木前辈
    def duanmu_high_lvl(self):
        box = self.get_like_word_box('端木前辈')
        if box is not None:
            self.click_box(box)
            self.click_like_word("跳过")
            return 'listen_is_difficult'
        return 'duanmu_high_lvl'

    # 听上去好难
    def listen_is_difficult(self):
        box = self.get_like_word_box('听上去好难')
        if box is not None:
            self.click_box(box)
            return 'work_hard'
        return 'listen_is_difficult'

    # 我会努力的
    def work_hard(self):
        box = self.get_like_word_box('我会努力的')
        if box is not None:
            self.click_box(box)
            return 'listen_yang_class'
        return 'work_hard'

# 介绍学院教程
    def listen_yang_class(self):
        box = self.get_like_word_box('介绍学院教程')
        if box is not None:
            self.click_box(box)
            return 'bai_give_to_me'
        return 'listen_yang_class'

    # 白露姐给
    def bai_give_to_me(self):
        box = self.get_like_word_box('白露姐给')
        if box is not None:
            self.click_box(box)
            self.click_like_word("跳过")
            return 'end'
        return 'bai_give_to_me'




config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
fb = Grade(config)
fb.run()