# coding=utf-8
from sqlalchemy import Column, Integer, VARCHAR, UniqueConstraint, Boolean
from sqlalchemy.ext.declarative import declarative_base

# 常量表
# protocol
HTTP_PROTOCOL = 0
HTTPS_PROTOCOL = 1
# type
TRANSPARENT = 0  # 透明
ANONYMOUS = 1  # 匿名

Base = declarative_base()


class Proxy(Base):
    __tablename__ = 'proxy'
    __table_args__ = (UniqueConstraint("protocol", "ip", "port", name="unique_protocol://ip:port"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(VARCHAR(16), nullable=False)
    port = Column(Integer, nullable=False)
    type = Column(Integer, nullable=False)
    protocol = Column(Integer, nullable=False, default=0)
    country = Column(VARCHAR(100), nullable=False)
    area = Column(VARCHAR(100), nullable=False)
    is_valid = Column(Boolean, nullable=False)
