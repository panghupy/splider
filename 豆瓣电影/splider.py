import requests
# 自动化测试工具
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import request, parse
from lxml import etree

# start += 15,每页15条数据
url = 'https://movie.douban.com/subject_search?search_text=%E7%BD%91&cat=1002&start=1'

kw = '成龙'
print(parse.quote(kw))
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
}
# 创建一个浏览器对象
driver = webdriver.Chrome(executable_path='/home/song/Desktop/chromedriver')
driver.get(url)
html = driver.page_source
response = etree.HTML(html)
cover_div_list = response.xpath('//div[@class="item-root"]')
# 得到每个电影的div
for item in cover_div_list:
    # 详情页链接
    url = item.xpath('./a/@href')[0]
    # 电影封面链接
    image = item.xpath('./a/img/@src')[0]

    detail_div = item.xpath('./div[@class="detail"]')[0]
    # 获取评分
    reaing_nums = item.xpath('.//span[@class="rating_nums"]/text()')[0]
    # 评论量
    comment_nums = item.xpath('.//span[@class="pl"]/text()')[0]
    print(type(str(comment_nums)))
    break

driver.close()
