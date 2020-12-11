import re
import requests
import base64
import json
import time
from bs4 import BeautifulSoup
from multiprocessing import Pool, Manager
import threading
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def Newqingqiu(id):
    header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.9',
              'Cache-Control': 'max-age=0',
              'Connection': 'keep-alive',
              'Cookie': 'xxx',
              'Host': 'gdx.cuit.edu.cn',
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
              }
    url='http://gdx.cuit.edu.cn/wlsys/stu/select_class.asp?num='
    url = url + str(id)
    req = requests.get(url, headers=header)
    req.encoding='gb2312'
    wyy = req.text[4205:]
    return wyy

def Check(ii):
    print("Hello I am ",ii)
    while True:
        try:
            New = Newqingqiu(ii)
        except Exception as e:
            print("New faild",ii)
        try:
            Old = Newqingqiu(ii)
        except Exception as e:
            print("old faild",ii)
        print(New)
        time.sleep(10)
        if(New != Old):
            send_email()

def send_email():
    from_addr = 'xxxx'  # 邮件发送账号
    to_addrs = 'xxx'  # 接收邮件账号
    qqCode = 'xxx'  # 授权码（这个要填自己获取到的）
    smtp_server = 'smtp.mxhichina.com'  # 固定写死
    smtp_port = 465  # 固定端口

    # 配置服务器
    stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    stmp.login(from_addr, qqCode)

    # 组装发送内容
    message = MIMEText('xxx', 'plain', 'utf-8')  # 发送的内容
    message['From'] = Header("xxx", 'utf-8')  # 发件人
    message['To'] = Header("xxxx", 'utf-8')  # 收件人
    subject = '可以抢课啦！！！！（物理）'
    message['Subject'] = Header(subject, 'utf-8')  # 邮件标题

    try:
        stmp.sendmail(from_addr, to_addrs, message.as_string())
    except Exception as e:
        print('邮件发送失败--' + str(e))
    print('邮件发送成功')

if __name__ == "__main__":

    for i in range(22,65):
        # 每循环一次创建一个子线程
        sub_thread = threading.Thread(target=Check,kwargs={"ii":i})
        # 启动子线程
        sub_thread.start()