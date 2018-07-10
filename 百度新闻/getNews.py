import requests
from lxml import etree
import json
import os

url = 'http://news.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
}
response = requests.get(url, headers=headers)
print(response.status_code)
result = etree.HTML(response.text)
# print(type(result))
# 热点要闻
novel_list = result.xpath('//div[@id="pane-news"]//ul//a')
# print(type(novel_list))
category = '热点要闻'
if not os.path.exists(category):
    os.mkdir(category)
for item in novel_list:
    title = item.xpath('./text()')[0]
    url = item.xpath('.//@href')[0]
    filename = category + '/' + title + '.html'
    hotnews_response = requests.get(url, headers=headers)
    hotnews_response.encoding = 'utf-8'
    hotnews_response = hotnews_response.text
    # print(hotnews_response)
    # with open(filename, 'w') as f:
    #     f.write(hotnews_response)

# 除了热点要闻以外其他分类都是异步请求


# 本地新闻
local_news_url = 'http://news.baidu.com/widget?id=LocalNews&ajax=json&t=1531143211718'
category = '本地新闻'
if not os.path.exists(category):
    os.mkdir(category)
response = requests.get(local_news_url, headers=headers)
print(response.status_code)
result = json.loads(response.text)["data"]["LocalNews"]["data"]["rows"]
for k, v in result.items():
    # print(v)
    for dic in v:
        if isinstance(dic, dict):
            print(dic["title"], dic["url"])
            title = dic["title"]
            url = dic["url"]
            filename = category + '/' + title + '.html'
            print(title, url)
            local_news_response = requests.get(url, headers=headers)
            local_news_response.encoding = 'utf-8'
            local_news_response = local_news_response.text
            with open(filename, 'w') as f:
                f.write(local_news_response)









