__author__ = 'dk'
##服务启动后, 会一直执行本脚本.(每5秒)
import requests
import config
import json
from generate_configure import main
import logger
_url = 'http://{0}:8080'

def check_ip(ip):
    msg = 'check ip {0}'.format(ip)
    logger.info(msg)
    url = _url.format(ip)
    try:
        _  = requests.get(url, timeout=10)
        msg = 'ip {0} connected'.format(ip)
        logger.info(msg)
        return True
    except BaseException as exp:
        msg = 'ip {0} not connected'.format(ip)
        logger.error(msg)
        return  False

if __name__ == '__main__':
    ##读取文件, 获取旧的ip
    with open(config.ip_fname) as fp:
        old_ip = json.load(fp)['ip']

    ##检测旧ip是否联通
    r = check_ip(ip = old_ip)
    #不通, 就重新生成
    if r == False :
        main()
    else:
        pass