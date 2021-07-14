import sys
import io
from urllib import request
import random
from urllib.parse import quote
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

#配置部分
cookie_str = ""
user_page = r''
plus_key = r''

# 登录后才能访问的网站
u1 = 'https://keylol.com/forum.php?mod=guide&view=my'
u2 = 'https://keylol.com/t' + str(random.randint(300000, 731527)) + '-1-1'
# plus webhook地址
u3h = "http://www.pushplus.plus/send/" + plus_key + "?title=" + quote("其乐论坛自动签到", 'utf-8') + "&content="
u3 = ""


def auto(url):
    global u3
    try:
        req = request.Request(url)
        # 设置cookie
        req.add_header('cookie', cookie_str)
        # 设置请求头
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

        resp = request.urlopen(req)
        print("已访问：", url, " 状态码：", resp.getcode())
        u3 += "已访问：" + url + " 状态码：" + str(resp.getcode()) + "<br>"
    except Exception as e:
        u3 += e.__str__() + "<br>"


def getCredit(url):
    global u3
    try:
        req = request.Request(url)
        # 设置cookie
        req.add_header('cookie', cookie_str)
        # 设置请求头
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 '
                       'Safari/537.36')

        resp = request.urlopen(req)
        bs = BeautifulSoup(resp.read().decode('utf-8'), "html.parser")
        em = bs.findAll('li')[100]
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


if __name__ == '__main__':
    print("其乐自动签到 By Moecola.com")
    print("--------------------------")
    print("签到开始")
    u3 += '签到开始<br>'
    getCredit(user_page)
    auto(u1)
    auto(u2)
    print("签到结束")
    u3 += '签到结束<br>'
    getCredit(user_page)
    u3 = quote(u3, 'utf-8')
    pushMsg(u3h + u3)
