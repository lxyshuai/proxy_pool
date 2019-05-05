import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

from proxy_pool.proxy_getter.proxy_fetch import ProxyFetch
from proxy_pool.validator.raw_proxy_check import RawProxyCheck
from proxy_pool.validator.valid_proxy_check import ValidProxyCheck


def run_apscheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(func=ValidProxyCheck().check_valid_proxy,
                      trigger=IntervalTrigger(seconds=10),
                      next_run_time=datetime.datetime.now(),
                      id="valid_proxy_check")
    scheduler.add_job(func=RawProxyCheck().check_raw_proxy,
                      trigger=IntervalTrigger(seconds=10),
                      id="raw_proxy_check")
    scheduler.add_job(ProxyFetch.call_all_proxy_getter,
                      trigger=IntervalTrigger(minutes=5),
                      next_run_time=datetime.datetime.now(),
                      id="proxy_fetch")
    scheduler.start()


if __name__ == '__main__':
    run_apscheduler()
