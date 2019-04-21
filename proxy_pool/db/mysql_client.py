# coding=utf-8
from sqlalchemy import create_engine, func, exc
from sqlalchemy.orm import sessionmaker, scoped_session

from proxy_pool.config.settings import DATABASE
from proxy_pool.db.client import Client
from proxy_pool.db.model.proxy import Proxy, Base
from proxy_pool.utils.logger import db_logger


class MysqlClient(Client):
    def __init__(self):
        """
        初始化Mysql数据库连接
        """
        db_string = "mysql+mysqlconnector://{username}:{password}@{host}:{port}/{name}?charset={charset}".format(
            username=DATABASE["USER"],
            password=DATABASE["PASSWORD"],
            host=DATABASE["HOST"],
            port=DATABASE["PORT"],
            name=DATABASE["NAME"],
            charset=DATABASE["CHARSET"]
        )
        self.engine = create_engine(db_string)
        session_factory = sessionmaker(bind=self.engine)
        self.session = scoped_session(session_factory)

    def init_db(self):
        """
        初始化数据库结构
        :return: None
        :rtype: None
        """
        Base.metadata.create_all(self.engine)

    def drop_db(self):
        """
        删除数据库数据及结构
        :return:
        :rtype:
        """
        Base.metadata.drop_all(self.engine)

    def insert(self, proxy_dict):
        """
        插入proxy
        :param proxy_dict: {
            "ip": "111.111.111.111",
            "port": 111,
            "type": 0/1,
            "protocol": 0/1,
            "country": "xxx",
            "area": "xxxx",
            "is_valid": True/False
        }
        :type proxy_dict: dict[str,str/int/bool]
        :return: None
        :rtype: None
        """
        proxy = Proxy(ip=proxy_dict['ip'],
                      port=proxy_dict['port'],
                      type=proxy_dict['type'],
                      protocol=proxy_dict['protocol'],
                      country=proxy_dict['country'],
                      area=proxy_dict['area'],
                      is_valid=proxy_dict["is_valid"]
                      )
        try:
            self.session.add(proxy)
            self.session.commit()
        except exc.IntegrityError as e:
            # 重复插入抛出IntegrityError，捕获异常并不插入重复数据
            self.session.rollback()

    def delete(self, condition_dict):
        """
        删除proxy
        :param condition_dict: {
            "ip": "111.111.111.111",
            "port": 111,
            "type": 0/1,
            "protocol": 0/1,
            "country": "xxx",
            "area": "xxxx",
            "is_valid": True/False
        }
        用于筛选的条件，仅需要列出要筛选的条件
        :type condition_dict: dict[str,str/int/bool]
        :return: 删除proxy的数量
        :rtype: int
        """
        query = self.session.query(Proxy)
        condition_list = self.determine_condition(condition_dict)
        for condition in condition_list:
            query = query.filter(condition)
        delete_number = query.delete()
        self.session.commit()
        return delete_number

    def update(self, condition_dict, update_dict):
        """
        更新proxy
        :param condition_dict: {
            "ip": "111.111.111.111",
            "port": 111,
            "type": 0/1,
            "protocol": 0/1,
            "country": "xxx",
            "area": "xxxx",
            "is_valid": True/False
        }
        用于筛选的条件，仅需要列出要筛选的条件
        :type condition_dict: dict[str,str/int/bool]
        :param update_dict: {
            "ip": "111.111.111.111",
            "port": 111,
            "type": 0/1,
            "protocol": 0/1,
            "country": "xxx",
            "area": "xxxx",
            "is_valid": True/False
        }
        改变后的值，仅需要列出改变的值
        :type update_dict: dict[str,str/int/bool]
        :return: 改变proxy的数量
        :rtype: int
        """
        query = self.session.query(Proxy)
        condition_list = self.determine_condition(condition_dict)
        for condition in condition_list:
            query = query.filter(condition)
        update_value_dict = self.determine_update_value(update_dict)
        update_number = query.update(update_value_dict)
        self.session.commit()
        return update_number

    def select(self, count, condition_dict):
        """
        获取proxy
        :param count: 需要获取的数量,当为0的时候视为获取全部
        :type count: int
        :param condition_dict: {
            "ip": "111.111.111.111",
            "port": 111,
            "type": 0/1,
            "protocol": 0/1,
            "country": "xxx",
            "area": "xxxx",
            "is_valid": True/False
        }
        用于筛选的条件，仅需要列出要筛选的条件
        :type condition_dict: dict[str,str/int/bool]
        :return: [Proxy1, Proxy2...]
        :rtype: list[Proxy]
        """
        query = self.session.query(Proxy)
        condition_list = self.determine_condition(condition_dict)
        for condition in condition_list:
            query = query.filter(condition)
        if count == 0:
            db_logger.info("get all proxy")
            return query.order_by(func.rand()).all()
        else:
            db_logger.info("get %s proxy" % count)
            return query.order_by(func.rand()).limit(count).all()

    @staticmethod
    def determine_condition(condition_dict):
        condition_list = []
        if condition_dict.get("ip"):
            condition_list.append(Proxy.ip == condition_dict.get("ip"))
        if condition_dict.get("port"):
            condition_list.append(Proxy.port == condition_dict.get("port"))
        if condition_dict.get("protocol"):
            condition_list.append(Proxy.protocol == condition_dict.get("protocol"))
        if condition_dict.get("type"):
            condition_list.append(Proxy.type == condition_dict.get("type"))
        if condition_dict.get("country"):
            condition_list.append(Proxy.country == condition_dict.get("country"))
        if condition_dict.get("area"):
            condition_list.append(Proxy.area == condition_dict.get("area"))
        if condition_dict.get("is_valid"):
            condition_list.append(Proxy.is_valid == condition_dict.get("is_valid"))
        return condition_list

    @staticmethod
    def determine_update_value(update_dict):
        update_value_dict = {}
        if update_dict.get("ip"):
            update_value_dict[Proxy.ip] = update_dict.get("ip")
        if update_dict.get("port"):
            update_value_dict[Proxy.port] = update_dict.get("port")
        if update_dict.get("protocol"):
            update_value_dict[Proxy.protocol] = update_dict.get("protocol")
        if update_dict.get("type"):
            update_value_dict[Proxy.type] = update_dict.get("type")
        if update_dict.get("country"):
            update_value_dict[Proxy.country] = update_dict.get("country")
        if update_dict.get("area"):
            update_value_dict[Proxy.area] = update_dict.get("area")
        if update_dict.get("is_valid"):
            update_value_dict[Proxy.is_valid] = update_dict.get("is_valid")
        return update_value_dict
