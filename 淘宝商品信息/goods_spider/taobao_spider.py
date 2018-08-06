import requests
from lxml import etree
from selenium import webdriver
import time
import json
import os

from 淘宝商品信息.DataTools import tools


# 解析数据,data：html页面
def parse_data(data):
    html = etree.HTML(data)
    # 得到商品div的列表
    print('新的一页-----------------------------')
    goods_div = html.xpath('//div[contains(@class,"J_MouserOnverReq")]')
    for goods in goods_div:
        title = ''
        title_list = goods.xpath('.//div[contains(@class,"title")]/a/text()')
        # 商品标题
        for i in title_list:
            title = (title + i.replace('\n', '')).strip().replace('/', '')
        print(title)
        # 商品价格
        price = goods.xpath('.//strong/text()')[0]
        print(price)
        # 付款人数
        pay_num = goods.xpath('.//div[@class="deal-cnt"]/text()')[0]
        print(pay_num)
        # 店名
        store_name = goods.xpath('.//a[contains(@class,"J_ShopInfo")]//span[last()]/text()')[0]
        print(store_name)
        # 存到本地
        save_json(title, price, pay_num, store_name)
        # 存到数据库
        save_database(title, price, pay_num, store_name)


# 定义一个方法，用来将数据存储到数据库

def save_database(title, price, pay_num, store_name):
    mysqlHelper = tools.MysqlHelper('localhost', 'root', '123456', 'taobao_db')
    mysqlHelper.connect()
    sql = 'insert into goods_data values(0,%s,%s,%s,%s)'
    params = [title, price, pay_num, store_name]
    mysqlHelper.insert(sql, params)


# 定义一个方法，使传入的数据构成一个字典并转换成json串存在本地
def save_json(title, price, pay_num, store_name):
    data = {
        "title": title,
        "price": price,
        "pay_num": pay_num,
        "store_name": store_name,
    }
    # 把python对象转换成json串儿
    json_data = json.dumps(data)
    # 写入本地文件
    with open('data.json', 'a') as f:
        f.write(json_data)


# 从淘宝搜索商品
def search_goods():
    kw = input('请输入查询关键字')
    '''抓取淘宝商品信息'''
    url = 'https://www.taobao.com/'
    # 实例化一个浏览器对象
    browser = webdriver.Chrome(executable_path='/home/song/Desktop/chromedriver')
    browser.get(url)
    browser.find_element_by_id('q').send_keys(kw)
    browser.find_element_by_css_selector('.btn-search.tb-bg').click()
    # 此时跳转到了搜索的商品列表页

    result = browser.page_source
    # 抓取100页商品信息
    for i in range(1, 101):
        # 让浏览器自动点击下一页
        js = "var q=document.documentElement.scrollTop=4100"
        browser.execute_script(js)
        time.sleep(3)
        browser.find_element_by_xpath('//div[@id="mainsrp-pager"]//a[@trace="srp_bottom_pagedown"]').click()
        result = browser.page_source
        parse_data(result)


def main():
    while True:
        option = input('请选择操作：1.搜索商品(淘宝网),2.查询商品信息(数据库),3.退出\n')
        if option == '1':
            search_goods()
        elif option == '2':
            get_data_from_database()
        elif option == '3':
            break
        else:
            print('输入有误，请重新输入')


# 定义一个从数据库中分页拿取数据的方法
def get_data_from_database():
    try:

        page = int(input("你想要查询第几页页数据，每页15条"))
    except:
        print("输入有误")
    mysqlHelper = tools.MysqlHelper('localhost', 'root', '123456', 'taobao_db')
    mysqlHelper.connect()
    page = (page - 1) * 15
    sql = 'select * from goods_data limit %s,15'
    params = [page]
    data = mysqlHelper.fetchall(sql, params)
    print(data)


if __name__ == '__main__':
    main()
