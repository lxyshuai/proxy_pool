import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from proxy_pool.proxy_getter.proxy_fetch import ProxyFetch
from proxy_pool.validator.raw_proxy_check import RawProxyCheck
from proxy_pool.validator.valid_proxy_check import ValidProxyCheck


def run_apscheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(ValidProxyCheck().check_valid_proxy, "interval", seconds=1,
                      next_run_time=datetime.datetime.now(),
                      id="valid_proxy_check")
    scheduler.add_job(RawProxyCheck().check_raw_proxy, "interval", minutes=1,
                      id="raw_proxy_check")
    scheduler.add_job(ProxyFetch.call_all_proxy_getter, "interval", minutes=5,
                      next_run_time=datetime.datetime.now(),
                      id="proxy_fetch")
    scheduler.start()


if __name__ == '__main__':
    run_apscheduler()
