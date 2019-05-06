from flask import Flask
from flask_restful import Resource, Api

from proxy_pool.config import settings
from proxy_pool.db import Client
from proxy_pool.db.model.proxy import HTTP_PROTOCOL, HTTPS_PROTOCOL
from proxy_pool.utils.check_proxy import check_proxy
from proxy_pool.utils.logger import api_logger

app = Flask(__name__)
api = Api(app)


class HttpProxy(Resource):
    def get(self):
        condition_dict = {
            "is_valid": True,
            "protocol": HTTP_PROTOCOL
        }
        proxy_list = Client.select(0, condition_dict)
        for proxy in proxy_list:
            if check_proxy(proxy):
                result_dict = {
                    "message": "Get a http proxy successfully",
                    "ip": proxy.ip,
                    "port": proxy.port,
                    "protocol": "http"
                }
                api_logger.info(
                    "ProxyCheck: %s://%s:%d validation pass" % (
                        "http" if proxy.protocol == HTTP_PROTOCOL else "https",
                        proxy.ip,
                        proxy.port
                    )
                )
                api_logger.info(
                    "Return %s://%s:%d" % (
                        "http" if proxy.protocol == HTTP_PROTOCOL else "https",
                        proxy.ip,
                        proxy.port
                    )
                )
                return result_dict
            else:
                api_logger.info(
                    "ProxyCheck: %s://%s:%d validation fail" % (
                        "http" if proxy.protocol == HTTP_PROTOCOL else "https",
                        proxy.ip,
                        proxy.port
                    )
                )
        else:
            result_dict = {
                "message": "Get a http proxy unsuccessfully",
            }
            api_logger.info("Return None")
            return result_dict


class HttpsProxy(Resource):
    def get(self):
        condition_dict = {
            "is_valid": True,
            "protocol": HTTPS_PROTOCOL
        }
        proxy_list = Client.select(0, condition_dict)
        for proxy in proxy_list:
            if check_proxy(proxy):
                result_dict = {
                    "message": "Get a https proxy successfully",
                    "ip": proxy.ip,
                    "port": proxy.port,
                    "protocol": "https"
                }
                api_logger.info(
                    "ProxyCheck: %s://%s:%d validation pass" % (
                        "http" if proxy.protocol == HTTP_PROTOCOL else "https",
                        proxy.ip,
                        proxy.port
                    )
                )
                api_logger.info(
                    "Return %s://%s:%d" % (
                        "http" if proxy.protocol == HTTP_PROTOCOL else "https",
                        proxy.ip,
                        proxy.port
                    )
                )
                return result_dict
            else:
                api_logger.info(
                    "ProxyCheck: %s://%s:%d validation fail" % (
                        "http" if proxy.protocol == HTTP_PROTOCOL else "https",
                        proxy.ip,
                        proxy.port
                    )
                )
        else:
            result_dict = {
                "message": "Get a https proxy unsuccessfully",
            }
            api_logger.info("Return None")
            return result_dict


api.add_resource(HttpProxy, '/http_proxy')
api.add_resource(HttpsProxy, '/https_proxy')

if __name__ == '__main__':
    app.run(host=settings.SERVER_API['HOST'], port=settings.SERVER_API['PORT'])
