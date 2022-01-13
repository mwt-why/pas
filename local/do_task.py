from local_file_util import read_as_list
import multiprocessing as mp
from script.entrance.ty import TYEnter
import os
import copy

config = {'ip': '192.168.31.92', 'area': '长歌行', 'type': '1', 'account': '', 'password': ''}
cur_dir = os.path.split(os.path.realpath(__file__))[0]
phone_path = cur_dir + "/config/devices"  # 设备路径


def create_task(ip):
    task = copy.deepcopy(config)
    ns = ip.split(".")
    task["id"] = ns[3]  # id取ip地址的最后位
    task["ip"] = ip
    task['serverType'] = 'local'
    enter = TYEnter()
    enter.execute(task)


def create_process(ip):
    ctx = mp.get_context('spawn')
    p = ctx.Process(target=create_task, args=(ip,))
    p.start()


"""
此处开始本地调用
"""
if __name__ == '__main__':
    ip_list = read_as_list(phone_path)
    for ip in ip_list:
        create_process(ip)
