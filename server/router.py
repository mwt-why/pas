from http_util import HttpUtil


# 获取可用的任务
def get_tasks():
    return HttpUtil.get("task/usable")


# 检查设备状态
def get_dev_status(serial):
    return HttpUtil.get("device/" + serial)


# 使用设备
def use_dev(serial):
    return HttpUtil.put("device/" + serial)


# 释放设备
def release_dev(serial):
    return HttpUtil.put("device/" + serial)
