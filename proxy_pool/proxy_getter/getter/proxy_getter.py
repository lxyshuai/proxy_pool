# coding=utf-8
from abc import ABCMeta, abstractmethod


class ProxyGetter(object):
    """
    代理获取抽象类
    """
    __metaclass__ = ABCMeta

    @classmethod
    @abstractmethod
    def get_proxy(cls):
        """
        爬取代理网站，返回代理
        @return:
            string:"192.168.1.1:8000"
        """
        raise NotImplementedError("Abstract method has not been implemented")
