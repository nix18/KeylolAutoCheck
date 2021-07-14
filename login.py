import json
import re
import requests


class DiscuzLogin:
    proxies = {

    }

    def __init__(self, hostname, username, password, questionid='0', answer=None, proxies=None):
        self.session = requests.session()
        self.hostname = hostname
        self.username = username
        self.password = password
        self.questionid = questionid
        self.answer = answer
        if proxies:
            self.proxies = proxies

    @classmethod
    def user_login(cls, hostname, username, password, questionid='0', answer=None, proxies=None):
        user = DiscuzLogin(hostname, username, password, questionid, answer, proxies)
        user.login()

    # def form_hash(self):
    #     rst = self.session.get(f'https://{self.hostname}/member.php?mod=logging&action=login').text
    #     loginhash = re.search(r'<div id="main_message_(.+?)">', rst).group(1)
    #     formhash = re.search(r'<input type="hidden" name="formhash" value="(.+?)" />', rst).group(1)
    #     return loginhash, formhash

    def login(self):
        # loginhash, formhash = self.form_hash()
        login_url = f'https://{self.hostname}/member.php?mod=logging&action=login&loginsubmit=yes&inajax=1'
        formData = {
            'referer': f'https://{self.hostname}/',
            'loginfield': self.username,
            'username': self.username,
            'password': self.password,
            'questionid': self.questionid,
            'answer': self.answer,
            'cookietime': 2592000
        }
        login_rst = self.session.post(login_url, proxies=self.proxies, data=formData)
        if self.session.cookies.get('dz_2132_auth'):
            print(f'Welcome {self.username}!')
            cookies_dict = requests.utils.dict_from_cookiejar(self.session.cookies)
            # 使用utils.dict_from_cookiejar 将cookies数据类型转化为字典
            cookies_str = json.dumps(cookies_dict).replace("{", "").replace("\"", "").replace(": ", "=").replace(",",
                                                                                                                ";").replace(
                "}", "")
            return cookies_str
        else:
            raise ValueError('Verify Failed! Check your username and password!')


def login(name, pwd):
    return DiscuzLogin.user_login('keylol.com', name, pwd)


