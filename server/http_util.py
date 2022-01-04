import urllib3
import json
from env.env import Env

ERROR = -99
http = urllib3.PoolManager()


class HttpUtil:
    base_url = ""

    def set_base_url(self):
        env = Env()
        url = env.get_value("manage_server.url")
        self.base_url = url

    def get(self, path, params=None):
        return self.request("GET", self.base_url + "/" + path, params)

    def post(self, path, data=None):
        return self.request("POST", self.base_url + "/" + path, data)

    def put(self, path, data=None):
        return self.request("PUT", self.base_url + "/" + path, data)

    @staticmethod
    def request(way, url, payload):
        if payload:
            resp = http.request(
                way,
                url,
                body=json.dumps(payload),
                headers={'Content-Type': 'application/json'}
            )
        else:
            resp = http.request(
                way,
                url
            )
        if resp.status == 200:
            result = json.loads(resp.data)
            return result["data"]
        else:
            return ERROR
