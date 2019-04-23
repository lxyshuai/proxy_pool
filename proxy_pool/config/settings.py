# coding=utf-8
"""
配置文件
"""

# Mysql数据库配置
DATABASE = {
    "TYPE": "MySQL",
    "HOST": "127.0.0.1",
    "PORT": 3306,
    "NAME": "proxy",
    "USER": "root",
    "PASSWORD": "vae680300",
    "CHARSET": "utf8"
}

# PROXY_GETTER配置
PROXY_GETTER = [
    "XicidailiProxyGetter"
]

# 配置 WEB REST API服务
SERVER_API = {
    "HOST": "127.0.0.1",  # 监听ip, 0.0.0.0 监听所有IP
    "PORT": 8080  # 监听端口
}
