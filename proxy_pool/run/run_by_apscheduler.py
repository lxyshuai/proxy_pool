import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from proxy_pool.api.proxy_api import api_run
from proxy_pool.proxy_getter.proxy_fetch import ProxyFetch
from proxy_pool.validator.raw_proxy_check import RawProxyCheck
from proxy_pool.validator.valid_proxy_check import ValidProxyCheck

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(ValidProxyCheck().check_valid_proxy, "interval", seconds=10,
                      next_run_time=datetime.datetime.now(),
                      id="valid_proxy_check")
    scheduler.add_job(RawProxyCheck().check_raw_proxy, "interval", minutes=1, id="raw_proxy_check")
    scheduler.add_job(ProxyFetch.call_all_proxy_getter, "interval", minutes=10,
                      next_run_time=datetime.datetime.now(),
                      id="proxy_fetch")
    scheduler.add_job(api_run, id='api_run')
    scheduler.start()
