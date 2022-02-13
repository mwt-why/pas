"""
这是脚本总体的入口的父类
提供了一些公用的方法和方便反射实例化子各个脚本的入口程序
"""
from server.router import Router
from local.local_file_util import get_account, get_excel_sheet
from script.ty.checkout_role import CheckoutRole


class BaseEnter:
    task = None
    serial = ""
    router = Router()
    roles = None
    role_index = 0  # 其实是下一个角色在roles中的下标
    cur_account = None
    FLG_EXCEL = 0
    FLG_FILE = 1
    FLG_CUSTOM = 2
    sheet = None
    next_row = 1

    def run(self, serial):
        self.serial = serial
        task = self.prepare(serial)
        if task is None:
            return
        self.execute(task)
        self.end()

    """
    开始之前的准备工作
    """

    def prepare(self, serial):
        task = self.router.get_task(serial)
        report = {
            "code": 1,
            "msg": "标记任务",
            "taskId": task["id"],
            "dev": serial
        }
        self.router.feedback(report)
        return task

    """
    子类的执行逻辑
    """

    def execute(self, task):
        pass

    """
    脚本结束的善后工作
    """

    def end(self, task):
        report = {
            "code": 0,
            "msg": "完成一项子任务",
            "taskId": task["id"],
            "dev": self.serial
        }
        self.router.feedback(report)
        self.router(self.serial)

    def get_account(self, flag=FLG_FILE):
        if flag == self.FLG_FILE:
            acc_pwd = self.get_account_from_file()
        elif flag == self.FLG_EXCEL:
            acc_pwd = self.get_account_from_excel()
        elif flag == self.FLG_CUSTOM:
            acc_pwd = self.get_account_from_custom()
        if acc_pwd is None:
            return None
        self.task["account"] = acc_pwd[0]
        self.task["password"] = acc_pwd[1]
        return acc_pwd[0]

    @staticmethod
    def get_account_from_custom():
        acc_pwd = ["u9bxdt@163.com", "zha729"]
        return acc_pwd

    @staticmethod
    def get_account_from_file():
        return get_account()

    def get_account_from_excel(self):
        if self.sheet is None:
            self.sheet = get_excel_sheet("/home/why/Downloads/统计账号更正版.xlsx", "Sheet2")
        acc_col = "A" + str(self.next_row)
        pwd_col = "B" + str(self.next_row)
        acc_pwd = []
        acc = self.sheet[acc_col].value
        pwd = self.sheet[pwd_col].value
        if (acc is not None) and (pwd is not None):
            self.next_row = self.next_row + 1
            acc_pwd.append(acc)
            acc_pwd.append(pwd)
            return acc_pwd
        return None

    def checkout_role(self):
        print("角色下标", self.role_index)
        if self.task["roleNum"] < (self.role_index + 1):
            print("已无角色,结束该账号的统计")
            return None
        result = CheckoutRole(self.task).run()
        return result
