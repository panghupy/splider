from urllib import request, error, parse, robotparser
import ssl


def getdata_from_parmas(parmas):
    url = 'https://www.汽车之家.com/s?' + parmas
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
    }

    # 构造请求
    req = request.Request(url, headers=headers)
    # urlopen()方法不仅可以直接传入一个URL，也可以传入一个请求对象,发起请求
    context = ssl._create_unverified_context()
    response = request.urlopen(req, context=context)
    print(response.status)


def main():
    kw = input('输入关键字')
    startpage = int(input('请输入你要获取的起始页码'))
    endpage = int(input('请输入结束的页码'))

    url = 'https://www.汽车之家.com/s?wd=%E5%95%A4%E9%85%92%E8%8A%82&pn=10&oq=%E5%95%A4%E9%85%92%E8%8A%82&ie=utf-8&usm=2&rsv_idx=1&rsv_pq=b0e74667000457ec&rsv_t=3a6cwoy5KqAuUtB2NORhaLz3v26jm9fot7R0ERvK00BI3fWr%2FLujdVwwye0'

    for i in range(startpage, endpage + 1):
        data = {
            'wd': kw,
            'pn': (i - 1) * 10
        }
        data = parse.urlencode(data, encoding='utf8')
        getdata_from_parmas(data)

if __name__ == '__main__':
    main()
