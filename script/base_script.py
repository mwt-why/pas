import logging as LOG
from abc import ABC, abstractmethod


class BaseScript(ABC):
    @abstractmethod
    def start():
        LOG.warn("this is a abtract method,please implement it")

    def run(self):
        method_name = start()
        while(True):
            method = getattr(self, method_name)
            method_na = method()
