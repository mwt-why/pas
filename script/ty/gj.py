from script.base_script import BaseScript


class Gj(BaseScript):
    def start(self):
        self.click_x_y(1687, 950)
        return ''

    def notice(self):
        box = self.get_word_box('接受任务')
        if box is not None:
            self.click_box(box)
        return 'notice'

    def do_task(self):
        self.click_word('跳过')
        return 'do_task'
