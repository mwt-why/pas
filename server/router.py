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

    # 释放账号
    def release_account(self, account):
        return self.http_util.put("account/" + account)

    # 反馈信息给服务器
    def feedback(self, report):
        return self.http_util.put("feedback", report)

    # 获取除自己以外的账号
    def list_role_except_me(self, params):
        return self.http_util.get("role", params)

    # 给账号添加角色
    def add_role(self, params):
        return self.http_util.put("role", params)
