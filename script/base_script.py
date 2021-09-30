import logging as LOG
from abc import ABC, abstractmethod


class BaseScript(ABC):
    @abstractmethod
    def start():
        LOG.info("start script")
