from server.http_util import HttpUtil


class Router:
    http_util = None

    def __init__(self):
        self.http_util = HttpUtil()
        self.http_util.set_base_url()

    def pre_dev_serial(self):
        return self.http_util.get("device/preDevSerial")

    def get_task(self, serial):
        return self.http_util.get("subTask/usable/" + serial)

    # 检查设备状态
    def get_dev_status(self, serial):
        return self.http_util.get("device/" + serial)

    # 使用设备
    def use_dev(self, serial):
        return self.http_util.put("device/" + serial)

    # 释放设备
    def release_dev(self, serial):
        return self.http_util.put("device/" + serial)

    # 反馈信息给服务器
    def feedback(self, report):
        return self.http_util.put("feedback", report)
