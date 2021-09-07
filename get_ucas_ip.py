import requests
import json
##使用dnspod的api来获取最新的解析记录。
from config import login_id, login_token, domain_id
LOGIN_TOKEN = '{0},{1}'.format(login_id,login_token)
headers = {
    'content-type':'application/x-www-form-urlencoded'
}
def get_record_id():
    url = 'https://dnsapi.cn/Record.List'
    data = 'login_token={0}&format=json&domain_id={1}&sub_domain=nps&record_type=A&offset=0&length=3'.format(LOGIN_TOKEN,domain_id)
    record_list = requests.post(url,data=data,headers = headers).json()
    print(record_list)
    return record_list['records'][0]['id']

def get_record_info():
    record_id = get_record_id()
    print(record_id)
    url = 'https://dnsapi.cn/Record.Info'
    data = 'login_token={0}&format=json&domain_id={1}&record_id={2}'.format(LOGIN_TOKEN, domain_id, record_id)
    record = requests.post(url, data=data, headers=headers).json()
    return  record

def get_ucas_ip():
    record = get_record_info()
    ip = record['record']['value']
    return  ip
if __name__ == '__main__':
    get_record_info()
