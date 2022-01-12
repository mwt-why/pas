from script.ty.start import Start
from script.base_enter import BaseEnter


class TY(BaseEnter):
    task = None

    def execute(self, task):
        self.task = task
        start = Start()
        start.run()
        script_name = self.task['scriptName']
        print('i am ' + script_name)
