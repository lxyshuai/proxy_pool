from Queue import Queue

from proxy_pool.db import Client
from proxy_pool.utils.logger import valid_proxy_check_logger
from proxy_pool.validator.proxy_check_thread import ProxyCheckThread


class ValidProxyCheck(object):
    def __init__(self):
        self.valid_proxy_queue = Queue()

    def start_threads(self, thread_number=5):
        thread_list = list()
        for _ in range(thread_number):
            thread_list.append(ProxyCheckThread(self.valid_proxy_queue, valid_proxy_check_logger))

        for thread in thread_list:
            thread.daemon = True
            thread.start()

        for thread in thread_list:
            thread.join()

    def put_queue(self):
        condition_dict = {
            "is_valid": True
        }
        for valid_proxy in Client.select(count=0, condition_dict=condition_dict):
            self.valid_proxy_queue.put(valid_proxy)

    def check_valid_proxy(self):
        self.put_queue()
        valid_proxy_check_logger.info("get %d proxy" % self.valid_proxy_queue.qsize())
        if not self.valid_proxy_queue.empty():
            valid_proxy_check_logger.info("Start check valid proxy")
            self.start_threads()
        valid_proxy_check_logger.info("Check valid proxy complete! sleep 10s")
