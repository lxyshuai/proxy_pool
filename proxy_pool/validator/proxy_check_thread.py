# coding=utf-8

from Queue import Empty
from threading import Thread

import requests

from proxy_pool.db import Client
from proxy_pool.db.model.proxy import HTTP_PROTOCOL, HTTPS_PROTOCOL


class ProxyCheckThread(Thread):
    def __init__(self, queue, logger):
        Thread.__init__(self)
        self.queue = queue
        self.logger = logger

    @classmethod
    def check_proxy(cls, proxy):
        # 代理是http代理
        if proxy.protocol == HTTP_PROTOCOL:
            proxies = {"http": "http://%s:%s" % (proxy.ip, proxy.port)}
            test_url = 'http://httpbin.org/ip'
        # 代理是https代理
        elif proxy.protocol == HTTPS_PROTOCOL:
            proxies = {"https": "https://%s:%s" % (proxy.ip, proxy.port)}
            test_url = 'https://httpbin.org/ip'
        try:
            # 超过10秒的代理认为无效代理
            response = requests.get(url=test_url, proxies=proxies, timeout=10)
            if response.status_code == 200 and response.json().get("origin"):
                return True
            else:
                return False
        except Exception:
            return False

    def run(self):
        while True:
            try:
                proxy = self.queue.get_nowait()
            except Empty:
                break
            if self.check_proxy(proxy):
                if not proxy.is_valid:
                    condition_dict = {
                        "ip": proxy.ip,
                        "port": proxy.port,
                        "protocol": proxy.protocol
                    }
                    update_dict = {
                        "is_valid": True
                    }
                    Client.update(condition_dict, update_dict)
                self.logger.info(
                    "ProxyCheck: %s://%s:%d validation pass" % (
                        "http" if proxy.protocol == HTTP_PROTOCOL else "https",
                        proxy.ip,
                        proxy.port
                    )
                )
            else:
                condition_dict = {
                    "ip": proxy.ip,
                    "port": proxy.port,
                    "protocol": proxy.protocol
                }
                Client.delete(condition_dict)
                self.logger.info(
                    "ProxyCheck: %s://%s:%d validation fail" % (
                        "http" if proxy.protocol == HTTP_PROTOCOL else "https",
                        proxy.ip,
                        proxy.port
                    )
                )
        self.logger.info("end")
