# coding=utf-8
import time

from bs4 import BeautifulSoup

from proxy_pool.db import Client
from proxy_pool.db.model.proxy import HTTPS_PROTOCOL, HTTP_PROTOCOL, TRANSPARENT, ANONYMOUS
from proxy_pool.proxy_getter.getter.proxy_getter import ProxyGetter
from proxy_pool.utils.html_downloader import HtmlDownloader
from proxy_pool.utils.logger import proxy_getter_logger


class JiangxianliProxyGetter(ProxyGetter):
    url = "http://ip.jiangxianli.com/"

    @classmethod
    def get_proxy(cls):
        """
        爬取免费IP代理库网站html，解析后获得代理将代理加入数据库
        """
        request = HtmlDownloader()
        proxy_getter_logger.info("Start get Jiangxianli proxy")
        try:
            for page in range(1, 3):
                url = cls.url + "?page=" + str(page)
                html = request.download(url=url)
                # 从html中提取proxy
                soup = BeautifulSoup(html, features="html.parser")
                tbody = soup.find("tbody")
                tr_list = tbody.find_all("tr")
                for tr in tr_list:
                    td_list = tr.find_all("td")
                    proxy_dict = {
                        "country": "China",
                        "ip": unicode(td_list[1].string),
                        "port": int(td_list[2].string),
                        "area": unicode(td_list[5].string),
                        "type": TRANSPARENT if td_list[3] == u"透明" else ANONYMOUS,
                        "protocol": HTTP_PROTOCOL if td_list[4].string == "HTTP" else HTTPS_PROTOCOL,
                        "is_valid": False
                    }
                    proxy_getter_logger.info(proxy_dict)
                    Client.insert(proxy_dict)
            proxy_getter_logger.info("End get Jiangxianli proxy successfully")
        except Exception as e:
            proxy_getter_logger.warn("End get Jiangxianli proxy unsuccessfully, because %s" % e)


JiangxianliProxyGetter.get_proxy()