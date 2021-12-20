"""
这是脚本总体的入口的父类
提供了一些公用的方法和方便反射实例化子各个脚本的入口程序
"""
from server.router import Router


class BaseEnter:
    serial = ""
    router = Router()

    def run(self, serial):
        self.serial = serial
        task = self.prepare(serial)
        if task is None:
            self.router.release_dev(serial)
            return
        self.execute(task)
        # self.end()

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
