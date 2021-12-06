from script.base_script import BaseScript


class Sy(BaseScript):
    def start(self):
        self.click_x_y(1460, 900)
        return 'answer'

    def answer(self):
        box = self.get_answer_box()
        if box is not None:
            self.click_box(box)
        box = self.get_like_word_box('答案拖到此处')
        if box is not None:
            ans_box = self.get_answer_box()
            if ans_box is not None:
                from_x = float(box[0][0])
                from_y = float(box[0][1])
                to_x = float(ans_box[1][0])
                to_y = float(ans_box[1][1])
                self.d.swipe_points([(from_x, from_y), (to_x, to_y)], 0.2)
                box = self.get_like_word_box('确认提交')
                if box is not None:
                    self.click_box(box)
        box = self.get_like_word_box('你已经答完了今天所有的题目')
        if box is not None:
            box = self.get_like_word_box('确定')
            if box is not None:
                self.click_box(box)
                return 'end'
        return 'answer'

    def get_answer_box(self):
        ans_arr = ['A', 'B', 'C', 'D']
        for a in ans_arr:
            box = self.get_like_word_box(a)
            if box is not None:
                return box
        return None


config = {'id': '0', 'ip': '192.168.31.184', 'role_name': '徐离珊', 'task': 'rc', 'area': '长歌行'}
task = Sy(config)
task.run()
