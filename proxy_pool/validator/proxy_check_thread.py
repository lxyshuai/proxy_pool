# coding=utf-8
import threading
from threading import Thread

from proxy_pool.db import Client
from proxy_pool.utils.logger import proxy_check_logger

mutex = threading.Lock()


class ProxyCheckThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        # super(ProxyCheckThread, self).__init__()
        self.queue = queue

    @classmethod
    def check_proxy(cls, proxy):
        # Todo:测试Proxy是否有效
        return True

    def run(self):
        while True:
            mutex.acquire()
            if self.queue.qsize():
                print self.queue.qsize()
                proxy = self.queue.get()
                mutex.release()
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
                        proxy_check_logger.info("ProxyCheck: {} validation pass".format(proxy.ip))
                else:

                    condition_dict = {
                        "ip": proxy.ip,
                        "port": proxy.port,
                        "protocol": proxy.protocol
                    }
                    Client.delete(condition_dict)
                    proxy_check_logger.info("ProxyCheck: {} validation fail".format(proxy.ip))
            else:
                mutex.release()
                break
        proxy_check_logger.info("end")
