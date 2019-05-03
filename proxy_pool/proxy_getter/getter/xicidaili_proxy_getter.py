# coding=utf-8
import time

from bs4 import BeautifulSoup

from proxy_pool.db import Client
from proxy_pool.db.model.proxy import HTTPS_PROTOCOL, HTTP_PROTOCOL, TRANSPARENT, ANONYMOUS
from proxy_pool.proxy_getter.getter.proxy_getter import ProxyGetter
from proxy_pool.utils.html_downloader import HtmlDownloader
from proxy_pool.utils.logger import proxy_getter_logger


class XicidailiProxyGetter(ProxyGetter):
    # 透明URL
    transparent_url = 'http://www.xicidaili.com/nn/'
    # 高匿URL
    anonymous_url = 'http://www.xicidaili.com/nt/'

    @classmethod
    def get_proxy(cls):
        """
        爬取西刺代理网站html，解析后获得代理将代理加入数据库
        """
        request = HtmlDownloader()
        proxy_getter_logger.info("Start get Xicidaili proxy")
        # 爬取透明proxy
        for page in range(1, 5):
            # 拼接url
            url = cls.transparent_url + str(page)
            html = request.download(url=url)
            # 从html中提取proxy
            soup = BeautifulSoup(html, features="html.parser")
            table = soup.find("table", id="ip_list")
            for tr in table.find_all("tr")[1:]:
                td_list = tr.find_all("td")
                proxy_dict = {
                    "country": "China",
                    "ip": unicode(td_list[1].string),
                    "port": int(td_list[2].string),
                    "area": unicode(td_list[3].find("a").string if td_list[3].find("a") else ""),
                    "type": TRANSPARENT,
                    "protocol": HTTPS_PROTOCOL if td_list[5].string == "HTTPS" else HTTP_PROTOCOL,
                    "is_valid": False
                }
                proxy_getter_logger.info(proxy_dict)
                Client.insert(proxy_dict)
            # 防止被代理网站反爬，添加间隔时间2s
            time.sleep(1)

        # 爬取高匿proxy
        for page in range(1, 5):
            # 拼接url
            url = cls.anonymous_url + str(page)
            html = request.download(url=url)
            # 从html中提取proxy
            soup = BeautifulSoup(html, features="html.parser")
            table = soup.find("table", id="ip_list")
            for tr in table.find_all("tr")[1:]:
                td_list = tr.find_all("td")
                proxy_dict = {
                    "country": "China",
                    "ip": unicode(td_list[1].string),
                    "port": int(td_list[2].string),
                    "area": unicode(td_list[3].find("a").string if td_list[3].find("a") else ""),
                    "type": ANONYMOUS,
                    "protocol": HTTPS_PROTOCOL if td_list[5].string == "HTTPS" else HTTP_PROTOCOL,
                    "is_valid": False
                }
                proxy_getter_logger.info(proxy_dict)
                Client.insert(proxy_dict)
            # 防止被代理网站反爬，添加间隔时间2s
            time.sleep(1)
