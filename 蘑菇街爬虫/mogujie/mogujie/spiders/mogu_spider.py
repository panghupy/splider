# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import re
import json
from mogujie.items import MogujieItem


class MoguSpiderSpider(scrapy.Spider):
    name = 'mogu_spider'
    allowed_domains = ['mogujie.com']
    start_urls = ['http://mogujie.com/']

    def start_requests(self):
        # browser = webdriver.Chrome(executable_path='/home/song/Desktop/chromedriver')
        # browser.get('http://mogujie.com/')
        # response = browser.page_source
        # with open('index.html', 'w')as f:
        #     f.write(response)
        # browser.close()
        yield scrapy.Request('http://mogujie.com/', callback=self.parse)

    def parse(self, response):
        with open('index.html', 'r')as f:
            response = f.readlines()
        result = ''
        for item in response:
            print(type(item))
            result += item
        print('*' * 100)
        print(type(result))
        pattern = re.compile('href="(http://list.mogujie.com/book/.*?)">.*?</a>')
        result = re.findall(pattern, result)
        for url in result:
            # with open('url.txt', 'a')as f:
            #     f.write(url + '\n')
            yield scrapy.Request(url=url, callback=self.parse_goods_list)

    def parse_goods_list(self, response):
        title = response.xpath('//title/text()').extract_first().split('：')[0]
        # title = ''
        # for i in goods_title:
        #     title +=i
        #     if i == '：':
        #         break
        # print(title,response.url)
        acm = response.url.split('?')[1]
        action = response.url.split('/')[4]
        print(acm, action)
        goods_url_example = 'http://list.mogujie.com/search?_version=8193&ratio=3%3A4&cKey=15&page=2&sort=pop&ad=0&fcid=10056587&action=sports&acm=3.mce.1_10_1hhdg.110548..5fV4dqYTJuESw.pos_0-m_407806-sd_119-mf_15261_990938-idx_0-mfs_17-dm1_5000&ptp=1._mf1_1239_15261.0.0.3QE6yetJ&_=1532597829467'
        for page in range(1, 2):
            goods_url = goods_url_example.replace(
                'acm=3.mce.1_10_1hhdy.110544..9XpX0qYTgjGRI.pos_1-m_407815-sd_119-mf_15261_990938-idx_0-mfs_89-dm1_5000',
                acm).replace('page=1', 'page=' + str(page)).replace('action=sports', 'action=' + action)
            print(goods_url)
            yield scrapy.Request(goods_url, callback=self.get_json_data, meta={'action': action})

    def get_json_data(self, response):
        # category = response.meta['action']
        # print('*' * 300)
        # print(response.url)
        # result = response.text[44:-2]
        # # print(result)
        # json_data = json.loads(result, encoding='utf-8')
        # print(type(json_data))
        # with open('goods_data.json', 'w')as f:
        #     f.write(result)
        # for i in json_data['result']['wall']['docs']:
        #     item = MogujieItem()
        #     # 商品分类
        #     item['category'] = category
        #     # 商品名称
        #     item['title'] = i['title']
        #     # 现价
        #     item['price'] = i['price']
        #     # 原价
        #     item['orgPrice'] = i['orgPrice']
        #     # 累计销售量
        #     item['sale'] = i['sale']
        #     print(i['title'],category)
        #     # yield item
        print('ok')