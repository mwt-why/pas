"""
这是脚本总体的入口的父类
提供了一些公用的方法和方便反射实例化子各个脚本的入口程序
"""


class BaseEnter:
    task = None

    def __init__(self, task):
        self.task = task

    def run(self):
        self.prepare()
        self.execute()
        self.end()

    """
    开始之前的准备工作
    """

    def prepare(self):
        pass

    """
    子类的执行逻辑
    """

    def execute(self):
        pass

    """
    脚本结束的善后工作
    """

    def end(self):
        pass
