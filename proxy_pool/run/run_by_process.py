import datetime
from multiprocessing import Process

from apscheduler.schedulers.blocking import BlockingScheduler

from proxy_pool.api.proxy_api import app
from proxy_pool.proxy_getter.proxy_fetch import ProxyFetch
from proxy_pool.validator.raw_proxy_check import RawProxyCheck
from proxy_pool.validator.valid_proxy_check import ValidProxyCheck


def raw_proxy_check_run():
    scheduler = BlockingScheduler()
    scheduler.add_job(RawProxyCheck().check_raw_proxy, "interval", minutes=1, id="raw_proxy_check")
    scheduler.start()


def valid_proxy_check_run():
    scheduler = BlockingScheduler()
    scheduler.add_job(ValidProxyCheck().check_valid_proxy, "interval", seconds=10,
                      next_run_time=datetime.datetime.now(),
                      id="valid_proxy_check")
    scheduler.start()


def proxy_fetch_run():
    scheduler = BlockingScheduler()
    scheduler.add_job(ProxyFetch.call_all_proxy_getter, "interval", minutes=10,
                      next_run_time=datetime.datetime.now(),
                      id="proxy_fetch")
    scheduler.start()


def api_run():
    app.run(host="127.0.0.1", port=8080)


if __name__ == '__main__':
    process_list = list()
    process1 = Process(target=raw_proxy_check_run, name='raw_proxy_check_run')
    process_list.append(process1)
    process2 = Process(target=valid_proxy_check_run, name='valid_proxy_check_run')
    process_list.append(process2)
    process3 = Process(target=proxy_fetch_run, name='proxy_fetch_run')
    process_list.append(process3)
    process4 = Process(target=api_run, name='api_run')
    process_list.append(process4)

    for p in process_list:
        p.daemon = True
        p.start()
    for p in process_list:
        p.join()
