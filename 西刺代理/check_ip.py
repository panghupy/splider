'''此程序用来检测代理IP是否有效'''
from urllib import request, error, parse
import ssl
import re


class CheckIp(object):
    def __init__(self, ip, port, scheme):
        self.ip = ip
        self.port = port
        self.scheme = scheme
        self.proxy_argument = {self.scheme: self.ip + ':' + self.port}
        self.url = 'https://www.汽车之家.com'

    def create_request(self):
        '''构造一个使用代理的请求'''
        httpHandler = request.HTTPHandler()
        httpsHandler = request.HTTPSHandler()
        proxyHandler = request.ProxyHandler(self.proxy_argument)
        self.opener = request.build_opener(httpsHandler, httpHandler, proxyHandler)
        # 构造请求对象
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
        }
        if self.scheme == 'https':
            self.context = ssl._create_unverified_context()
        else:
            self.context = None

    def check(self):
        '''发起请求，检测ip，有效则返回True，否则返回False'''
        self.create_request()
        self.req = request.Request(self.url, headers=self.headers, context=self.context)
        response = self.opener.open(self.req)
        if response.status == 200:
            return True

        else:
            return False
