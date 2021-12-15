import time
from multiprocessing import Process
from router import get_tasks
from router import get_dev_status
from router import use_dev
from router import feedback
from script.base_enter import BaseEnter


class Scheduler:
    scripts = None

    def __init__(self):
        self.schedule()
        self.scripts = BaseEnter.__subclasses__()

    def schedule(self):
        while True:
            tasks = get_tasks()
            if len(tasks) == 0:
                time.sleep(3)
                continue
            for task in tasks:
                serial = task["serial"]
                if self.dev_is_usable(serial):
                    script = self.resolve_task(task)
                    if script:
                        p = Process(target=self.create_task, args=(script,))
                        p.start()
                    else:
                        report = {
                            "id": task["id"],
                            "reason": "无效脚本,该脚本无法被解析"
                        }
                        feedback(report)

    @staticmethod
    def dev_is_usable(serial):
        status = get_dev_status(serial)
        if status == 0:
            return True
        return False

    """
    获取脚本对象
    """

    def resolve_task(self, task):
        name = task['scriptName']
        for script in self.scripts:
            if script.__name__ == name:
                model_module = __import__('model')
                m_py = getattr(model_module, 'm')
                obj = getattr(m_py, script)
                return obj(task)
        return None

    @staticmethod
    def create_task(script):
        script.run()
