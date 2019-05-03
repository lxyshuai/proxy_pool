import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from proxy_pool.validator.valid_proxy_check import ValidProxyCheck

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(ValidProxyCheck().check_valid_proxy, "interval", seconds=10,
                      next_run_time=datetime.datetime.now(),
                      id="valid_proxy_check")
    scheduler.start()
