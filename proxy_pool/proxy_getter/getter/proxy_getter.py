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
        爬取西刺代理网站html，解析后获得代理将代理加入数据库
        """
        raise NotImplementedError("Abstract method has not been implemented")
