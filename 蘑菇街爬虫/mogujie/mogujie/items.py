# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MogujieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    orgPrice = scrapy.Field()
    sale = scrapy.Field()
    # 商品分类
    category = scrapy.Field()
    # 商品名称
    # print(i['title'])
    # # 现价
    # print(i['price'])
    # # 原价
    # print(i['orgPrice'])
    # # 累计销售量
    # print(i['sale'])
