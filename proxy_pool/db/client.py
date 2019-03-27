# coding=utf-8
from abc import ABCMeta, abstractmethod


class Client(object):
    """
    数据库连接抽象类
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_db(self):
        """
        初始化数据库
        :return:
        :rtype:
        """
        raise NotImplementedError("Abstract method has not been implemented")

    @abstractmethod
    def drop_db(self):
        """
        删除数据库
        :return:
        :rtype:
        """
        raise NotImplementedError("Abstract method has not been implemented")

    @abstractmethod
    def insert(self, proxy_dict):
        raise NotImplementedError("Abstract method has not been implemented")

    @abstractmethod
    def delete(self, condition_dict):
        raise NotImplementedError("Abstract method has not been implemented")

    @abstractmethod
    def update(self, condition_dict, update_dict):
        raise NotImplementedError("Abstract method has not been implemented")

    @abstractmethod
    def select(self, count, condition_dict):
        raise NotImplementedError("Abstract method has not been implemented")
