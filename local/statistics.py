from local.local_file_util import read_as_list
from local.local_task import LocalTask
import os

cur_dir = os.path.split(os.path.realpath(__file__))[0]
phone_path = cur_dir + "/config/devices"  # 设备路径
task_type = "statistics"


def general():
    ip_list = read_as_list(phone_path)
    for ip in ip_list:
        LocalTask(ip, task_type)


if __name__ == '__main__':
    general()
