import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from proxy_pool.proxy_getter.proxy_fetch import ProxyFetch

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(ProxyFetch.call_all_proxy_getter, "interval", minutes=10,
                      next_run_time=datetime.datetime.now(),
                      id="proxy_fetch")
    scheduler.start()
