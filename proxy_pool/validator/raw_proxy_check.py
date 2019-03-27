from Queue import Queue

from proxy_pool.db import Client
from proxy_pool.utils.logger import proxy_check_logger
from proxy_pool.validator.proxy_check_thread import ProxyCheckThread


class RawProxyCheck(object):
    def __init__(self):
        self.raw_proxy_queue = Queue()

    def start_threads(self, thread_number=20):
        thread_list = list()
        for _ in range(thread_number):
            thread_list.append(ProxyCheckThread(self.raw_proxy_queue))

        for thread in thread_list:
            thread.daemon = True
            thread.start()

        for thread in thread_list:
            thread.join()

    def put_queue(self):
        condition_dict = {
            "is_valid": False
        }
        for raw_proxy in Client.select(count=0, condition_dict=condition_dict):
            self.raw_proxy_queue.put(raw_proxy)

    def check_raw_proxy(self):
        self.put_queue()
        if not self.raw_proxy_queue.empty():
            proxy_check_logger.info("Start check raw proxy")
            self.start_threads()
        proxy_check_logger.info("Check raw proxy complete! sleep 10s")
