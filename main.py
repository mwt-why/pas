import urllib3
import json
from script import ty
import _thread
import time

ERROR = -99
base_url = 'http://127.0.0.1:8080/'
http = urllib3.PoolManager()
cur_devs = set()


def get(url, params):
    url = base_url + url
    resp = http.request("GET", url)
    if resp.status == 200:
        result = json.loads(resp.data)
        return result['data']
    else:
        return ERROR


def script(mac):
    data = get('subTask/' + mac, 0)
    ty = Ty(data)
    ty.run()


def boot_thread(devs):
    try:
        for dev in devs:
            _thread.start_new_thread(script)
            cur_devs.add(dev)
    except:
        print('Error,线程无法启动')


while True:
    time.sleep(3)
    rec_devs = get('subTask/dev', 0)
    if rec_devs is None or len(rec_devs) == 0:
        continue
    if cur_devs != None or len(cur_devs) != 0:
        diff = (rec_devs).difference(cur_devs)
        if len(diff) != 0:
            boot_thread(diff)
