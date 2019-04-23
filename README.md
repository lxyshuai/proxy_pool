
爬虫IP代理池
=======
[![](https://img.shields.io/badge/Power%20by-%40lxyshuai-blue.svg)]()[![](https://img.shields.io/badge/language-Python-green.svg)](https://github.com/jhao104/proxy_pool)

    ______                        ______             _
    | ___ \_                      | ___ \           | |
    | |_/ / \__ __   __  _ __   _ | |_/ /___   ___  | |
    |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | |
    | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___
    \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____\
                           __ / /
                          /___ /

* 设计：[设计文档](https://github.com/lxyshuai/proxy_pool/blob/master/docs/%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.md)

* 支持版本: ![](https://img.shields.io/badge/Python-2.7-green.svg)

* 测试地址：

### 下载安装

* 下载源码:

```shell
git clone git@github.com:lxyshuai/proxy_pool.git

或者直接到https://github.com/lxyshuai/proxy_pool 下载zip文件
```

* 安装依赖:

```shell
pip install -r requirements.txt
```

* 配置proxy_pool/config/setting.py:

```shell
# proxy_pool/config/setting.py 为项目配置文件

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


```

* 初始化数据库：

```shell
# 目前暂时只支持Mysql
# 初始化数据库有两种方式

# 第一种
# 使用写好的init_db函数
>>> from proxy_pool.db import Client
>>> Client.init_db()
>>> Client.init_db()

# 第二种
# 去数据库中执行sql/proxy.sql

```

* 启动：

```shell
# 启动有两种方式

# 第一种
# apscheduler(多线程)
# 在proxy_pool/run下运行run_by_apscheduler.py
>>> python run_by_apscheduler.py

# 第二种
# 多进程
# 在proxy_pool/run下运行run_by_process.py
>>> python run_by_process.py

```

### 使用

​	启动过几分钟后就能看到抓取到的代理IP，你可以直接到数据库中查看

​	也可以通过api访问[http://127.0.0.1:8080](http://127.0.0.1:5010/)

* Api

| api | method | Description | arg|
| ----| ---- | ---- | ----|
| /get_http_proxy | GET | 获取一个可用的http代理 | None |
| /get_https_proxy | GET    | 获取一个可用的https代理 | None |

### 问题反馈

　　暂时不接受反馈。

