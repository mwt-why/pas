from script.ty.start import Start
from script.ty.statistics import Statistics
from script.ty.checkout_account import CheckoutAccount
from script.ty.pre_start import PreStart
from result.file_util import write_line
from script.base_enter import BaseEnter
from db.crud import CRUD
from script.ty.get_email import GetEmail


class TYEnter(BaseEnter):
    statistics_result = {}

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
        account = self.get_account(flag=self.FLG_EXCEL)
        if account is None:
            print("已经没有帐号，设备", self.task["ip"], "可以休息了")
            return
        self.cur_account = account
        print("切换帐号")
        result = CheckoutAccount(self.task).run()
        if result == 3:
            self.account_exception(account)
            self.statistics()
        print("准备开始游戏")
        result = PreStart(self.task).run()
        if result == 3:
            self.account_exception(account)
            self.statistics()
        print("切换角色")
        self.checkout_role()
        while True:
            print("一键领取邮件")
            GetEmail(self.task).run()
            print("开始统计")
            Statistics(self.task).run()
            print("可能出现弹窗，先去弹窗")
            PreStart(self.task).run()
            print("切换角色")
            has_role = self.checkout_role()
            if has_role is None:
                self.record_db()  # 保存到数据库
                self.rest()
                break
        self.statistics()
        print("结束统计")

    def rest(self):
        self.statistics_result.clear()
        self.cur_account = None
        self.role_index = 0
        self.roles = None

    def start_test(self):
        print("获取账号")
        account = self.get_account(flag=self.FLG_EXCEL)
        if account is None:
            print("已经没有帐号，设备", self.task["ip"], "可以休息了")
            return
        print("切换账号")
        CheckoutAccount(self.task).run()
        print("开始游戏")
        Start(self.task).run()
        self.start_test()

    def record(self):
        path = "/home/tommy/work/python/pas/result/statistics"
        s = '|'.join(self.statistics_result)
        write_line(path, s)
        self.statistics_result.clear()

    def record_db(self):
        print("持久化数据")
        self.statistics_result['account'] = self.cur_account
        crud = CRUD("ps", "result")
        print(self.statistics_result['account'])
        crud.insert_one(self.statistics_result)

    @staticmethod
    def account_exception(account):
        print("账号异常")
        crud = CRUD("ps", "result")
        account_exception = {account: "账号异常"}
        crud.insert_one(account_exception)

    def test(self):
        # self.done_role.append("孤独小萍")
        # result = CheckoutRole(self.task).run()
        # result = CurRole(self.task).run()
        result = Start(self.task).run()
        # result = Start1(self.task).run()
        # result = GetEmail(self.task).run()
        # result = Statistics(self.task).run()
        print(result)
