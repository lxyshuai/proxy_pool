from multiprocessing import Process

from proxy_pool.run.run_api import run_api
from proxy_pool.run.run_apscheduler import run_apscheduler

if __name__ == '__main__':
    process_list = list()
    process1 = Process(target=run_api, name='run_api')
    process_list.append(process1)
    process2 = Process(target=run_apscheduler, name='run_apscheduler')
    process_list.append(process2)

    for p in process_list:
        p.daemon = True
        p.start()
    for p in process_list:
        p.join()
