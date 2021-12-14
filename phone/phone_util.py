import uiautomator2 as u2
from phone import nmap_util


def test_connect_wifi(ip):
    try:
        d = u2.connect_wifi(ip)
        return d.device_info
    except u2.exceptions.ConnectError:
        return False


def test_connect_serial(serial):
    try:
        d = u2.connect(serial)
        return d.device_info
    except u2.exceptions.ConnectError:
        return False


def list_dev_info():
    dev_info_list = []
    ips = nmap_util.scan_device_ip()
    # 物理设备通过ip测试是否可连接
    for ip in ips:
        dev_info = test_connect_wifi(ip)
        if dev_info:
            simple_info = simplify_dev_info(dev_info, "physical")
            dev_info_list.append(simple_info)
    # 虚拟的通过serial测试连接
    # TODO
    return dev_info_list


def simplify_dev_info(dev_info, dev_type):
    return {
        "serial": dev_info["serial"],
        "brand": dev_info["brand"],
        "mac": dev_info["hwaddr"],
        "memory": dev_info["memory"]["total"],
        "width": dev_info["display"]["width"],
        "height": dev_info["display"]["height"],
        "type": dev_type
    }


def list_phone_ip_test():
    dev_info = test_connect_wifi("192.168.31.92")
    return [simplify_dev_info(dev_info, "physical")]
