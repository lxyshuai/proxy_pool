import json

from flask import Flask

from proxy_pool.db import Client

app = Flask(__name__)


@app.route("/get/")
def get():
    condition_dict = {
        "is_valid": True
    }
    proxy = Client.select(1, condition_dict)[0]
    result_dict = {
        "ip": proxy.ip,
        "port": proxy.port,
        "protocol": proxy.protocol
    }
    result = json.dumps(result_dict)
    return result


app.run(host="127.0.0.1", port=8080)
