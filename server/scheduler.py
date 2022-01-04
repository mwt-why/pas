import time
from multiprocessing import Process
from server.router import Router
from script.base_enter import BaseEnter
from env.env import Env
from script.registry import Registry


class Scheduler:
    scripts = None
    router = None
    env = None
    registry = None

    def __init__(self):
        self.init_env()
        self.scripts = BaseEnter.__subclasses__()

    def init_env(self):
        self.env = Env()
        self.router = Router()
        self.registry = Registry()

    def dev_dispatch(self):
        flag = True
        while flag:
            time.sleep(3)
            dev_serials = self.router.pre_dev_serial()
            if len(dev_serials) == 0:
                continue
            for serial in dev_serials:
                self.router.use_dev(serial)
                p = Process(target=self.script_dispatch, args=(serial,))
                p.start()

    """
    获取脚本对象
    """

    def resolve_script(self, serial):
        task = self.router.get_task(serial)
        if task is None:
            return None
        script_name = task["scriptName"]
        script_name = script_name.lower()
        try:
            return self.registry.get_script(script_name)
        except AttributeError:
            report = {
                "code": -99,
                "msg": "不存在的脚本",
                "taskId": task["id"],
                "dev": serial
            }
            self.router.feedback(report)
        return None

    def script_dispatch(self, serial):
        script = self.resolve_script(serial)
        if script:
            script.run(serial)