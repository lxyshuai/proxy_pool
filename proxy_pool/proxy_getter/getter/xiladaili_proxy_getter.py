# coding=utf-8
import time

from bs4 import BeautifulSoup

from proxy_pool.db import Client
from proxy_pool.db.model.proxy import HTTPS_PROTOCOL, HTTP_PROTOCOL, TRANSPARENT, ANONYMOUS
from proxy_pool.proxy_getter.getter.proxy_getter import ProxyGetter
from proxy_pool.utils.html_downloader import HtmlDownloader
from proxy_pool.utils.logger import proxy_getter_logger


class XiladailiProxyGetter(ProxyGetter):
    # 透明URL
    transparent_url = 'http://www.xiladaili.com/putong/'
    # 高匿URL
    anonymous_url = 'http://www.xiladaili.com/gaoni/'

    @classmethod
    def get_proxy(cls):
        """
        爬取西拉代理网站html，解析后获得代理将代理加入数据库
        """
        request = HtmlDownloader()
        proxy_getter_logger.info("Start get Xiladaili proxy")
        try:
            # 爬取透明proxy
            for page in range(1, 3):
                url = cls.transparent_url + str(page)
                html = request.download(url=url)
                # 从html中提取proxy
                soup = BeautifulSoup(html, features="html.parser")
                tbody = soup.find("tbody")
                tr_list = tbody.find_all("tr")
                for tr in tr_list:
                    td_list = tr.find_all("td")
                    proxy_dict = {
                        "country": "China",
                        "ip": unicode(td_list[0].string.split(":")[0]),
                        "port": int(td_list[0].string.split(":")[1]),
                        "area": unicode(td_list[3].string),
                        "type": TRANSPARENT,
                        "protocol": HTTP_PROTOCOL if td_list[1].string == u"HTTP代理" else HTTPS_PROTOCOL,
                        "is_valid": False
                    }
                    proxy_getter_logger.info(proxy_dict)
                    Client.insert(proxy_dict)

            # 爬取高匿proxy
            for page in range(1, 3):
                url = cls.anonymous_url + str(page)
                html = request.download(url=url)
                # 从html中提取proxy
                soup = BeautifulSoup(html, features="html.parser")
                tbody = soup.find("tbody")
                tr_list = tbody.find_all("tr")
                for tr in tr_list:
                    td_list = tr.find_all("td")
                    proxy_dict = {
                        "country": "China",
                        "ip": unicode(td_list[0].string.split(":")[0]),
                        "port": int(td_list[0].string.split(":")[1]),
                        "area": unicode(td_list[3].string),
                        "type": ANONYMOUS,
                        "protocol": HTTP_PROTOCOL if td_list[1].string == u"HTTP代理" else HTTPS_PROTOCOL,
                        "is_valid": False
                    }
                    proxy_getter_logger.info(proxy_dict)
                    Client.insert(proxy_dict)
            proxy_getter_logger.info("End get Xiladaili proxy successfully")
        except Exception as e:
            proxy_getter_logger.warn("End get Xiladaili proxy unsuccessfully, because %s" % e)