import yaml

env_path = "../env.yaml"


class Env:
    env_dict = {}

    def __init__(self):
        stream = open(env_path, 'r')
        self.env_dict = yaml.safe_load(stream)
        print(self.env_dict)

    def get_value(self, key):
        if len(self.env_dict) == 0:
            return None
        if (key is None) or (len(key) == 0):
            return None
        ks = key.split('.')
        # 如果只需要获取第一层的数据
        if len(ks) == 1:
            return self.env_dict[key]
        # 如果有多层的情况
        value = self.env_dict[ks[0]]
        for k in ks[1:]:
            value = value[k]
        return value
