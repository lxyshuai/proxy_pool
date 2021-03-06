# coding=utf-8
import time

from bs4 import BeautifulSoup

from proxy_pool.db import Client
from proxy_pool.db.model.proxy import HTTPS_PROTOCOL, HTTP_PROTOCOL, TRANSPARENT, ANONYMOUS
from proxy_pool.proxy_getter.getter.proxy_getter import ProxyGetter
from proxy_pool.utils.html_downloader import HtmlDownloader
from proxy_pool.utils.logger import proxy_getter_logger


class Data5uProxyGetter(ProxyGetter):
    url = 'http://www.data5u.com/'

    @classmethod
    def get_proxy(cls):
        """
        爬取无忧代理网站html，解析后获得代理将代理加入数据库
        """
        request = HtmlDownloader()
        proxy_getter_logger.info("Start get data5u proxy")
        try:
            html = request.download(url=cls.url)
            soup = BeautifulSoup(html, features="html.parser")
            ul_list = soup.find_all("ul", class_="l2")
            for ul in ul_list:
                li_list = ul.find_all("li")
                proxy_dict = {
                    "country": "China",
                    "ip": unicode(li_list[0].string),
                    "port": int(li_list[1].string),
                    "area": unicode(li_list[5].string),
                    "type": TRANSPARENT if li_list[2].string == u"透明" else ANONYMOUS,
                    "protocol": HTTPS_PROTOCOL if li_list[2].string == "https" else HTTP_PROTOCOL,
                    "is_valid": False
                }
                proxy_getter_logger.info(proxy_dict)
                Client.insert(proxy_dict)
            proxy_getter_logger.info("End get data5u proxy successfully")
        except Exception as e:
            proxy_getter_logger.warn("End get data5u proxy unsuccessfully, because %s" % e)
