from script.ty.start import Start
from script.base_enter import BaseEnter


class TYEnter(BaseEnter):
    task = None

    def execute(self, task):
        self.task = task
        start = Start(task)
        start.run()
