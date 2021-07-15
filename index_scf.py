# -*- coding: utf8 -*-
# 腾讯云SCF脚本，须在在线IDE终端，1- cd src , 2- pip install bs4 -t .
import io
import random
import sys
from urllib import request
from urllib.parse import quote

from bs4 import BeautifulSoup

from user import user

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

# 多用户配置：创建usr对象，并放入user_list中,例如user_list = [usr0, usr1]
usr0 = user(cookie_str="", user_page="", plus_key="")
# usr1 = user(cookie_str="",user_page="", plus_key="")
user_list = [usr0]

# 登录后才能访问的网站
u1 = 'https://keylol.com/forum.php?mod=guide&view=my'
u2 = 'https://keylol.com/t' + str(random.randint(300000, 731527)) + '-1-1'
# plus webhook地址
u3 = ""
uname = ""


def auto(user, url):
    global u3
    try:
        req = request.Request(url)
        # 设置cookie
        req.add_header('cookie', user.cookie_str)
        # 设置请求头
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

        resp = request.urlopen(req)
        print("【", resp.getcode(), "】", "已访问：", url)
        u3 += "【" + str(resp.getcode()) + "】" + "已访问：" + url + "<br>"
    except Exception as e:
        u3 += e.__str__() + "<br>"


def getCredit(user, url):
    global u3, uname
    try:
        req = request.Request(url)
        # 设置cookie
        req.add_header('cookie', user.cookie_str)
        # 设置请求头
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 '
                       'Safari/537.36')

        resp = request.urlopen(req)
        bs = BeautifulSoup(resp.read().decode('utf-8'), "html.parser")
        em = bs.findAll('li')[100]
        uname = bs.find("h2", {'class': 'mbn'}).text
        print(em.text)
        u3 += em.text + "<br>"
    except Exception as e:
        u3 += e.__str__() + "<br>"


def pushMsg(url):
    req = request.Request(url)
    # 设置请求头
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 '
                   'Safari/537.36')
    resp = request.urlopen(req)
    print("推送消息结果：", str(resp.read(), 'utf-8'))


def autoCheck(user):
    global u3, uname
    u3 = ""
    uname = ""
    u3h = "http://www.pushplus.plus/send/" + user.plus_key + "?title=" + quote("其乐论坛自动签到", 'utf-8') + "&content="
    print("其乐自动签到 By Moecola.com")
    print("--------------------------")
    print("【签到开始】")
    u3 += '【签到开始】 '
    getCredit(user, user.user_page)
    auto(user, u1)
    auto(user, u2)
    print("【签到结束】")
    u3 += '【签到结束】 '
    getCredit(user, user.user_page)
    print(uname, "签到完成")
    u3 += "<br>" + uname + "签到完成"
    u3 = quote(u3, 'utf-8')
    pushMsg(u3h + u3)


def main_handler(event, context):
    for u in user_list:
        autoCheck(u)

