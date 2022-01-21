"""
这是脚本总体的入口的父类
提供了一些公用的方法和方便反射实例化子各个脚本的入口程序
"""
from server.router import Router
from local.local_file_util import get_account
from script.ty.checkout_role import CheckoutRole
from script.ty.cur_role import CurRole


class BaseEnter:
    task = None
    serial = ""
    router = Router()
    done_role = []
    cur_role = None

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

    def get_account(self):
        acc_pwd = get_account()
        if acc_pwd is None:
            return None
        self.task["account"] = acc_pwd[0]
        self.task["password"] = acc_pwd[1]
        return acc_pwd[0]

    def get_cur_account_roles(self):
        result = CurRole(self.task).run()
        print("当前用户所有角色：", self.done_role)
        return result

    def checkout_role(self):
        done_role_num = len(self.done_role)
        if self.task["roleNum"] == done_role_num:
            return None
        result = CheckoutRole(self.task).run()
        return result
