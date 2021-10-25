import urllib3
import json

ERROR = -99
base_url = 'http://127.0.0.1:8080/'
http = urllib3.PoolManager()


def get(url, params):
    url = base_url + url
    resp = http.request("GET", url)
    if resp.status == 200:
        result = json.loads(resp.data)
        return result['data']
    else:
        return ERROR


def script(mac):
    # 根据mac地址获取任务
    data = get('subTask/'+mac,0)
    # 把所有东西装到config中
    print(data)
    # 把config传递到脚本中
    # 启动脚本


data = get('subTask/dev', 0)
script(data[0])
