__author__ = 'dk'
##DNSPod的域名信息

#1. 域名ID
domain_id = '87463236'
#2.login id和token
login_id = '256963'
login_token='aad32b9ddd498666aea8c3522f1b3c30'


## 反向代理配置信息
proxy = [
    {
    'LAN_ip':'127.0.0.1',
    'LAN_port':'3389',
    'remark':'remote desktop',
	'Server_port':'53390'
    },
    {
    'LAN_ip':'192.168.255.82',
    'LAN_port':'59527',
    'remark':'1080ti',
	'Server_port':'59527'
    },
    {
    'LAN_ip':'192.168.255.81',
    'LAN_port':'22',
    'remark':'titan',
	'Server_port':'59528'
    },	
]

## 配置文件路径(不要修改, 按照固定目录放置文件)
conf_fname = r"D:\windows_amd64_client\conf\npc.conf"

## 保存ip的文件
ip_fname = r"D:\windows_amd64_client\ip.json"

## 日志文件
log_fname =  r"D:\windows_amd64_client\log"

## ip保活检查时间(单位： 秒)
time= 5