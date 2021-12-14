import urllib3
import json
from env.env import Env

ERROR = -99
http = urllib3.PoolManager()


class HttpUtil:
    __base_url__ = ""

    def __int__(self, base_url):
        if len(base_url) != 0:
            self.__base_url__ = base_url
        else:
            self.__set_base_url__()

    def __set_base_url__(self):
        url = Env.get_value("manage_server.url")
        self.__base_url__ = url

    def get(self, path, params):
        return self.__request__("GET", self.__base_url__ + "/" + path, params)

    def post(self, path, data):
        return self.__request__("POST", self.__base_url__ + "/" + path, data)

    def put(self, path, data):
        return self.__request__("PUT", self.__base_url__ + "/" + path, data)

    @staticmethod
    def __request__(way, url, payload):
        resp = http.request(
            way,
            url,
            fields=payload
        )
        if resp.status == 200:
            result = json.loads(resp.data)
            return result["data"]
        else:
            return ERROR
