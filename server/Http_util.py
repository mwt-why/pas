import urllib3
import json

ERROR = -99
http = urllib3.PoolManager()


class HttpUtil:
    base_url = ''

    def __int__(self, base_url):
        self.base_url = base_url

    def get(self, url, params):
        return self.request("GET", self.base_url + '/' + url, params)

    def post(self, url, data):
        return self.request("POST", self.base_url + '/' + url, data)

    @staticmethod
    def request(way, url, payload):
        resp = http.request(
            way,
            url,
            fields=payload
        )
        if resp.status == 200:
            result = json.loads(resp.data)
            return result['data']
        else:
            return ERROR
