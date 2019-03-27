import importlib

from proxy_pool.config.settings import PROXY_GETTER


class ProxyFetch(object):
    @staticmethod
    def call_all_proxy_getter():
        module = importlib.import_module("proxy_pool.proxy_getter.getter")
        for proxy_getter in PROXY_GETTER:
            proxy_getter_class = getattr(module, proxy_getter)
            proxy_getter_class.get_proxy()
