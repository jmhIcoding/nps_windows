__author__ = 'dk'
from github import  Github
import platform
import os
import json
from get_ucas_ip import get_ucas_ip
from config import proxy, conf_fname
import logger

###配置文件模板
conf_template="""[common]
server_addr={0}:8024
conn_type=tcp
vkey=(abcd1234)
auto_reconnection=true
crypt=true
compress=true
remark={3}@{1} CPU: {2}"""
proxy_temp="""
[{0}]
mode=tcp
target_addr={1}:{2}
server_port={3}"""

def generate_configuration(ip, proxies):
    conf = conf_template.format(ip,platform.node(),platform.processor(),os.environ['USERNAME'])
    for pro in proxies:
        _ = proxy_temp.format(pro['remark'], pro['LAN_ip'], pro['LAN_port'], pro['Server_port'])
        conf += _
    return conf

def main():
    ip = get_ucas_ip()
    proxies = proxy

    conf = generate_configuration(ip=ip, proxies = proxies)

    msg="Generate new configuration:\n{0}".format(conf)
    print(conf)
    logger.info(msg)

    with open(conf_fname,'w') as fp:
        fp.writelines(conf)
if __name__ == '__main__':
    main()
