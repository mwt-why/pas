import urllib3
import json

ERROR = -99
http = urllib3.PoolManager()


class HttpUtil:
    base_url = ''

    def __int__(self, base_url):
        self.base_url = base_url

    def get(self, url, params):
        http.request(
            'GET',
            self.base_url + '/' + url,
            fields=params
        )

    def post(self, url, data):

    @staticmethod
    def request(self, method, url, payload):
        resp = http.request(
            method,
            url,
            fields=payload
        )
        if resp.status == 200:
            result = json.loads(resp.data)
            return result['data']
        else:
            return ERROR
