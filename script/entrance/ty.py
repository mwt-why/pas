from script.ty.start import Start
from script.ty.statistics import Statistics
from script.ty.checkout_account import CheckoutAccount
from result.file_util import write_line
from script.base_enter import BaseEnter
from script.ty.start1 import Start1


class TYEnter(BaseEnter):
    statistics_result = []

    def execute(self, task):
        task['enter'] = self
        self.task = task
        task_type = task['task_type']
        method = getattr(self, task_type)
        method()

    def general(self):
        result = Start(self.task).run()
        print(result)

    def statistics(self):
        account = self.get_account()
        if account is None:
            print("已经没有帐号，设备", self.task["ip"], "可以休息了")
            return
        account = account + "|"
        self.statistics_result.append(account)
        print("切换帐号")
        CheckoutAccount(self.task).run()
        print("开始游戏")
        Start(self.task).run()
        self.get_cur_account_roles()
        while True:
            print("开始统计")
            Statistics(self.task).run()
            has_role = self.checkout_role()
            if has_role is None:
                self.record()
                break
            print("重新开始游戏")
            Start(self.task).run()
        self.statistics()
        print("结束统计")

    def record(self):
        path = "/home/tommy/work/python/pas/result/statistics"
        s = '|'.join(self.statistics_result)
        write_line(path, s)
        self.statistics_result.clear()

    def test(self):
        # result = CheckoutRole(self.task).run()
        # result = CurRole(self.task).run()
        # result = Start(self.task).run()
        result = Start1(self.task).run()
        print(result)
