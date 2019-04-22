import json

from flask import Flask

from proxy_pool.db import Client
from proxy_pool.db.model.proxy import HTTP_PROTOCOL, HTTPS_PROTOCOL

app = Flask(__name__)


@app.route("/get_http_proxy/")
def get_http_proxy():
    condition_dict = {
        "is_valid": True,
        "protocol": HTTP_PROTOCOL
    }
    proxy_list = Client.select(1, condition_dict)
    if proxy_list:
        proxy = Client.select(1, condition_dict)[0]
        result_dict = {
            "message": "Get a http proxy successfully",
            "ip": proxy.ip,
            "port": proxy.port,
            "protocol": "http"
        }
    else:
        result_dict = {
            "message": "Get a http proxy unsuccessfully",
        }
    result = json.dumps(result_dict)
    return result


@app.route("/get_https_proxy/")
def get_https_proxy():
    condition_dict = {
        "is_valid": True,
        "protocol": HTTPS_PROTOCOL
    }
    proxy_list = Client.select(1, condition_dict)
    if proxy_list:
        proxy = Client.select(1, condition_dict)[0]
        result_dict = {
            "message": "Get a https proxy successfully",
            "ip": proxy.ip,
            "port": proxy.port,
            "protocol": "https"
        }
    else:
        result_dict = {
            "message": "Get a https proxy unsuccessfully",
        }
    result = json.dumps(result_dict)
    return result


def api_run():
    app.run(host="127.0.0.1", port=8080)
