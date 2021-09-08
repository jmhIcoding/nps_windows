__author__ = 'dk'
import config
import generate_configure
import keep_alive
import os
import logger
import multiprocessing
import time
import json
import sys
def connect_remote_server():
        cmd = "D:\\windows_amd64_client\\npc_raw.exe -config=D:\\windows_amd64_client\\conf\\npc.conf"
        os.system(cmd)

def refresh_configure():
    generate_configure.main()

def get_old_ip():
    ##读取文件, 获取旧的ip
    with open(config.ip_fname) as fp:
        old_ip = json.load(fp)['ip']
    return  old_ip
if __name__ == '__main__':
    subproc = None
    subproc = multiprocessing.Process(target=connect_remote_server)
    subproc.start()
    msg = 'start process {0} for connecting nps remote server'.format(subproc.pid)
    logger.info(msg)
    while True:
        old_ip = get_old_ip()
        if keep_alive.check_ip(old_ip) == False:
            refresh_configure()
        else:
            time.sleep(config.time)

