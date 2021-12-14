import time
from router import get_tasks
from router import get_dev_status
from router import use_dev


class Scheduler:

    def __init__(self):
        self.schedule()

    def schedule(self):
        while True:
            tasks = get_tasks()
            if len(tasks) == 0:
                time.sleep(3)
                continue
            for task in tasks:
                serial = task["serial"]
                if self.dev_is_usable(serial):
                    use_dev(serial)
                    self.create_task(task)

    @staticmethod
    def dev_is_usable(self, serial):
        status = get_dev_status(serial)
        if status == 0:
            return True
        return False

    def create_task(self, task):
        pass
