import netifaces
import nmap


def get_default_gateway():
    return netifaces.gateways()['default'][netifaces.AF_INET][0]


def list_gateway_ip(gateway):
    ips = []
    for i in range(1, 256):
        ip = '{}{}'.format(gateway[:-1], str(i))
        ips.append(ip)
    return ips


def scan_survival_ip(ip):
    port_scanner = nmap.PortScanner()
    result = port_scanner.scan(hosts=ip, arguments='-sP')
    scan = result['scan']
    if scan:
        return scan
    return None


def scan_device_ip():
    devices = []
    gateway = get_default_gateway()
    ips = list_gateway_ip(gateway)
    for ip in ips:
        device = scan_survival_ip(ip)
        if device:
            devices.append(ip)
            print(ip, '->up')
        else:
            print(ip, '->down')
    return devices
