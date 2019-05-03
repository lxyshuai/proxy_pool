from proxy_pool.api.proxy_api import app
from proxy_pool.config import settings


def run_api():
    app.run(host=settings.SERVER_API['HOST'], port=settings.SERVER_API['PORT'])


if __name__ == '__main__':
    run_api()
