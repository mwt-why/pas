"""
入口注册器
"""
from script.entrance.ty import TY


class Registry:
    ty = TY()

    def get_script(self, name):
        return getattr(self, name)
