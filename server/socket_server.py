import socket
import json
import signal
from phone import phone_util

DEFAULT_LISTEN = 5


class SocketServer:
    STATUS = True
    server = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, address, port):
        self.server.bind((address, port))
        self.server.listen(DEFAULT_LISTEN)
        self.STATUS = True

    def run(self):
        print("socket_server启动")
        while self.STATUS:
            client, address = self.server.accept()
            flag = self.filter(client, address)
            if flag:
                self.controller(client)
            else:
                self.error_handle(client)

    def stop(self):
        self.STATUS = False

    # 过滤非法用户
    @staticmethod
    def filter(client, address):
        return True

    def controller(self, client):
        result = str(client.recv(1), "UTF-8")
        sig = self.verify(result)
        if sig == signal.DEVICES_LIST:
            self.do_device_list(client)
        else:
            self.error_handle(client)

    @staticmethod
    def verify(msg):
        if msg == '':
            return False
        return msg[0]

    # 错误处理
    @staticmethod
    def error_handle(client):
        msg = "-99"
        client.send(msg.encode('utf-8'))
        client.close()

    @staticmethod
    def do_device_list(client):
        # dev_info = phone_util.list_phone_ip_test()
        dev_info = phone_util.list_dev_info()
        dev_info = json.dumps(dev_info)
        dev_info = dev_info + "\n"
        client.send(dev_info.encode('utf-8'))
        client.close()
