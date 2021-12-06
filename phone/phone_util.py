import uiautomator2 as u2
from phone import nmap_util


def test_connect_wifi(ip):
    try:
        u2.connect_wifi(ip)
    except u2.exceptions.ConnectError:
        return False
    else:
        return True


def test_connect_serial(serial):
    try:
        u2.connect(serial)
    except u2.exceptions.ConnectError:
        return False
    else:
        return True


def list_phone_ip():
    ip_list = []
    ips = nmap_util.scan_device_ip()
    for ip in ips:
        if test_connect_wifi(ip):
            ip_list.append(ip)


def list_phone_ip_test():
    return ['192.168.43.23', '192.168.55']
