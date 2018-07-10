from urllib import request
import ssl
import re


def send_request(url, charset_code='utf-8', is_decode=True):
    '''封装一个函数来发起请求,需要传入目标url和网页编码,返回响应体内容'''

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
    }

    req = request.Request(url, headers=headers)
    response = request.urlopen(req, context=ssl._create_unverified_context())
    if is_decode:
        result = response.read().decode(charset_code)
    else:
        result = response.read()
    return result


def image_load(result, filename):
    '''把二进制字节流写入文件,request表示字节流,filename表示文件名'''
    with open(filename, 'wb') as f:
        f.write(result)




url = 'https://www.autohome.com.cn/all/2/#liststart'
result = send_request(url, charset_code='gb2312')

# re.S表示.也可以匹配换行符,很关键！！！
string = '<div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g29/M07/9F/84/120x90_0_autohomecar__ChcCSFs6MN6AM60kAAGGGapv-6Y467.jpg"></div>'
pattern = re.compile('<div.*?class="article-pic">.*?<img.*?src="(.*?)">.*?</div>.*?<h3>(.*?)</h3>', re.S)

result = re.findall(pattern, result)
for item in result:
    url = 'https:' + item[0]
    filename = '汽车之家/' + item[1].replace('/', '') + '.jpg'
    result = send_request(url, is_decode=False)
    image_load(result, filename)
