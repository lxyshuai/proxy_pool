import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from proxy_pool.validator.raw_proxy_check import RawProxyCheck

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(RawProxyCheck().check_raw_proxy, "interval", minutes=1,
                      next_run_time=datetime.datetime.now(),
                      id="raw_proxy_check")
    scheduler.start()
