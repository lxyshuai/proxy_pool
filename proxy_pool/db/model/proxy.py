# coding=utf-8
from sqlalchemy import Column, Integer, VARCHAR, UniqueConstraint, Boolean, types
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

# 常量表
# protocol
from proxy_pool.utils.convert import ip_to_int, int_to_ip

HTTP_PROTOCOL = 0
HTTPS_PROTOCOL = 1
# type
TRANSPARENT = 0  # 透明
ANONYMOUS = 1  # 匿名

Base = declarative_base()


class IPType(types.TypeDecorator):
    impl = INTEGER(unsigned=True)

    def process_bind_param(self, value, dialect):
        return ip_to_int(value)

    def process_result_value(self, value, dialect):
        if value:
            return int_to_ip(value)
        else:
            return None

    def process_literal_param(self, value, dialect):
        pass

    @property
    def python_type(self):
        pass


class Proxy(Base):
    __tablename__ = 'proxy'
    __table_args__ = (UniqueConstraint("protocol", "ip", "port", name="unique_protocol://ip:port"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(IPType, nullable=False)
    port = Column(Integer, nullable=False)
    type = Column(Integer, nullable=False)
    protocol = Column(Integer, nullable=False, default=0)
    country = Column(VARCHAR(100), nullable=False)
    area = Column(VARCHAR(100), nullable=False)
    is_valid = Column(Boolean, nullable=False)
