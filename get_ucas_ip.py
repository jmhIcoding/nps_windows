import requests
import json
##使用dnspod的api来获取最新的解析记录。
from config import login_id, login_token, domain_id, ip_fname
import logger
LOGIN_TOKEN = '{0},{1}'.format(login_id,login_token)
headers = {
    'content-type':'application/x-www-form-urlencoded'
}
def get_record_id():
    url = 'https://dnsapi.cn/Record.List'
    data = 'login_token={0}&format=json&domain_id={1}&sub_domain=nps&record_type=A&offset=0&length=3'.format(LOGIN_TOKEN,domain_id)
    record_list = requests.post(url,data=data,headers = headers).json()
    msg = 'Get DNS Record:\n {0}'.format(str(record_list))
    logger.info(msg)
    return record_list['records'][0]['id']

def get_record_info():
    record_id = get_record_id()
    url = 'https://dnsapi.cn/Record.Info'
    data = 'login_token={0}&format=json&domain_id={1}&record_id={2}'.format(LOGIN_TOKEN, domain_id, record_id)
    record = requests.post(url, data=data, headers=headers).json()
    return  record

def get_ucas_ip():

    record = get_record_info()
    ip = record['record']['value']
    with open(ip_fname,'w') as fp:
        json.dump({'ip':ip},fp)
    with open(r'C:\Windows\System32\drivers\etc\hosts', 'r') as fp:
        lines = fp.readlines()
    flag = False
    for index, line in  enumerate(lines):
        if 'nps.jmhicoding.xyz' in line:
            lines[index] = '{0} {1}'.format(ip, 'nps.jmhicoding.xyz')
            flag = True

    if flag == False:
        lines.append('\n{0} {1}'.format(ip, 'nps.jmhicoding.xyz'))

    with open(r'C:\Windows\System32\drivers\etc\hosts', 'w') as fp:
        fp.writelines(lines)

    msg = 'Get new ip ({0}) from DNSPod.'.format(ip)
    logger.info(msg)
    return  ip

if __name__ == '__main__':
    get_record_info()
