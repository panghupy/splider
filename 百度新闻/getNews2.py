import requests
from lxml import etree
import json
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
}

# 国内 http://news.baidu.com/widget?id=civilnews&t=1531180841713
# 国际 http://news.baidu.com/widget?id=InternationalNews&t=1531180841735
# 娱乐 http://news.baidu.com/widget?id=EnterNews&t=1531180841761
# 体育 http://news.baidu.com/widget?id=SportNews&t=1531180841831
# 财经 http://news.baidu.com/widget?id=FinanceNews&t=1531180841852
# 科技 http://news.baidu.com/widget?id=TechNews&t=1531180841878
# 军事 http://news.baidu.com/widget?id=MilitaryNews&t=1531180841917
# 互联网 http://news.baidu.com/widget?id=InternetNews&t=1531180841973
# 探索 http://news.baidu.com/widget?id=DiscoveryNews&t=1531180842069
# 女人 http://news.baidu.com/widget?id=LadyNews&t=1531180842097
# 健康 http://news.baidu.com/widget?id=HealthNews&t=1531180842245
# 经研究发现，以上借口返回的响应模板是一样的，可以把它们加入到一个字典，分类名为键，url为值，遍历来请求

url_dic = {
    '国内': 'http://news.baidu.com/widget?id=civilnews&t=1531180841713',
    '国际': 'http://news.baidu.com/widget?id=InternationalNews&t=1531180841735',
    '娱乐': 'http://news.baidu.com/widget?id=EnterNews&t=1531180841761',
    '体育': 'http://news.baidu.com/widget?id=SportNews&t=1531180841831',
    '财经': 'http://news.baidu.com/widget?id=FinanceNews&t=1531180841852',
    '科技': 'http://news.baidu.com/widget?id=TechNews&t=1531180841878',
    '军事': 'http://news.baidu.com/widget?id=MilitaryNews&t=1531180841917',
    '互联网': 'http://news.baidu.com/widget?id=InternetNews&t=1531180841973',
    '探索': 'http://news.baidu.com/widget?id=DiscoveryNews&t=1531180842069',
    '女人': 'http://news.baidu.com/widget?id=LadyNews&t=1531180842097',
    '健康': 'http://news.baidu.com/widget?id=HealthNews&t=1531180842245'
}
for category, url in url_dic.items():
    if not os.path.exists(category):
        os.mkdir(category)
    response = requests.get(url, headers=headers)
    print(response.status_code)
    with open('news.html', 'w') as f:
        f.write(response.text)
    # print(result)
    result = etree.HTML(response.text).xpath('//div[contains(@class,"l-left-col")]//li')
    # print(result)
    for item in result:
        title = item.xpath('.//a/text()')[0].replace('/','')
        url = item.xpath('.//a/@href')[0]
        print(title, url)
        # 获取标题链接的内容html
        response = requests.get(url, headers=headers).text
        filename = category + '/' + title + '.html'
        with open(filename, 'w') as f:
            f.write(response)
