from urllib import request, error
import ssl
import re
from 西刺代理.DataTools import tools


# 把东西写入文件
def write_file(filename, result, is_image=False):
    if not is_image:
        with open(filename, 'w') as f:
            f.write(result)
    else:
        with open(filename, 'wb') as f:
            f.write(result)


# 西刺代理网址
for page in range(1, 3):
    url = 'http://www.xicidaili.com/nn/' + str(page)

    # 自定义opener
    httpHandler = request.HTTPHandler()
    httpsHandler = request.HTTPSHandler(context=ssl._create_unverified_context())
    opener = request.build_opener(httpHandler, httpsHandler)

    # 构造请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
    }
    req = request.Request(url, headers=headers)
    response = opener.open(req)
    result = response.read().decode('utf8')

    # 得到ip地址、端口号、服务器地址、类型(http,https)、存活时间、验证时间的列表
    pattern = re.compile(
        'odd.*?country.*?<td>(.*?)</td>.*?td>(.*?)</td>.*?href.*?>(.*?)</a>.*?country.*?<td>(.*?)</td>.*?country.*?country.*?<td>(.*?)</td>.*?<td>(.*?)</',
        re.S)
    result = re.findall(pattern, result)

    # 接下来拿到所有的代理ip访问下面链接来进行测试
    http_url = 'www.dianping.com/'
    https_url = 'www.meituan.com/'
    # 首先拿到创建代理处理器所需要的数据:ip、端口、协议
    for item in result:
        ip = item[0]
        port = item[1]
        address = item[2]
        scheme = item[3]
        survival_time = item[4]
        verification_time = item[5]
        proxies = {item[3]: item[0] + ':' + item[1]}
        # 构造一个使用代理的请求
        httpHandler = request.HTTPHandler()
        httpsHandler = request.HTTPSHandler(context=ssl._create_unverified_context())
        proxyHandler = request.ProxyHandler(proxies)
        opener = request.build_opener(httpHandler, httpsHandler, proxyHandler)
        # 构造请求对象
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
        }
        # 不同的协议类型使用不同的url接口检测
        if scheme.lower == 'http':
            test_full_url = scheme.lower() + '://' + http_url
        else:
            test_full_url = scheme.lower() + '://' + https_url
        try:
            req = request.Request(test_full_url, headers=headers)
            test_response = opener.open(req)
            print(test_response.status)
            if test_response.status == 200:
                print('将可用代理数据写入数据库')
                tools.write_data(ip, port, address, scheme, survival_time, verification_time, page)
        except error.HTTPError as e:
            print(e.reason)
        except error.URLError as e:
            print(e.reason)
