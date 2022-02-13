from script.base_script import BaseScript
from script.base_script import EXIT


class PreStart(BaseScript):
    def start(self):
        return "close_everything"

    def always(self):
        box = self.get_like_word_box("自动")
        if box:
            return EXIT

    def close_everything(self):
        result = self.ocr()
        for r in result:
            s = self.drop_space(r[1])
            if "暂时不用" in s:
                self.click_box(r[0])
                break
            elif "取消" in s:
                self.click_box(r[0])
                break
            elif "开启云垂" in s:
                self.click_box(r[0])
                break
            elif "稍后" in s:
                self.click_box(r[0])
                break
            elif "今日不再弹出" in s:
                self.click_x_y(1985, 130)
                break
            elif "前去找回" in s:
                self.click_x_y(1663, 308)
                break
            elif "我知道了" in s:
                self.click_x_y(1663, 308)
                break
            elif "前往中心世界即有机会获得" in s:
                self.click_x_y(1985, 130)
            elif "取消" is s:
                self.click_box(r[0])
            elif "被封禁" in s:
                return "account_exception"
        self.click_x_y(70, 800)  # 挂机
        return "close_everything"
