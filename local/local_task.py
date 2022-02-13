import time
import easyocr
import copy
import os

from multiprocessing import Process
from multiprocessing import Queue
from script.entrance.ty import TYEnter
from local.local_file_util import read_as_list

cur_dir = os.path.split(os.path.realpath(__file__))[0]
phone_path = cur_dir + "/config/devices"  # 设备路径

config = {'task_type': '', 'ip': '192.168.31.92', 'area': '长歌行', 'type': '0', 'account': '1212@163.com',
          'serial': '936X1XHD9',
          'password': 'qus022',
          'isNewAccount': 1,
          'roleNum': 3}
reader = easyocr.Reader(['ch_sim', 'en'])


class LocalTask(object):

    def create_task(self, job, ip, request_q, receive_q):
        task = copy.deepcopy(config)
        task["id"] = self.get_id(ip)  # id取ip地址的最后位
        task["ip"] = ip
        task['serverType'] = 'local'
        task['task_type'] = job
        task['request_q'] = request_q
        task['receive_q'] = receive_q
        enter = TYEnter()
        enter.execute(task)

    @staticmethod
    def get_id(ip):
        ns = ip.split(".")
        return ns[3]

    def create_process(self, ip, job, request_q, receive_q):
        p = Process(target=self.create_task, args=(job, ip, request_q, receive_q,))
        p.start()

    def general(self, job):
        request_q = Queue(maxsize=1)
        receive_q = Queue(maxsize=1)
        ip_list = read_as_list(phone_path)
        for ip in ip_list:
            self.create_process(ip, job, request_q, receive_q)
        # orc处理器
        self.ocr_handle(request_q, receive_q)

    @staticmethod
    def ocr_handle(request_q, receive_q):
        while True:
            if request_q.empty():
                time.sleep(0.5)
                continue
            request = request_q.get()
            result = reader.readtext(request)
            receive_q.put(result)


if __name__ == '__main__':
    LocalTask().general(job="statistics")
    # LocalTask().general(job="test")
    # LocalTask().general(job="start_test")
