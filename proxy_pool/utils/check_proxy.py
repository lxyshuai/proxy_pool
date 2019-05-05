# coding=utf-8
import requests

from proxy_pool.db.model.proxy import HTTP_PROTOCOL, HTTPS_PROTOCOL


def check_proxy(proxy):
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
