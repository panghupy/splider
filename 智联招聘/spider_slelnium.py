import requests
import csv
import time
from lxml import etree
from selenium import webdriver
import sys

# 默认递归深度可以爬取980页
# 设置默认递归深度为10的10次方
# sys.setrecursionlimit(10 ** 10)
main_url = 'https://sou.zhaopin.com/?jl=530'

'''在智联招聘使用selenium模拟浏览器搜索职位，存储数据'''
# 创建浏览器对象
opt = webdriver.ChromeOptions()
opt.set_headless()
driver = webdriver.Chrome(executable_path='/home/song/Desktop/chromedriver')
driver.get(main_url)
# 获取搜索关键字

kw = '我我哦我我我'
driver.find_element_by_xpath('//div[@class="zp-search-common"]//input').send_keys(kw)
driver.find_element_by_xpath('//a[@class="zp-search-btn zp-blue-button"]').click()
time.sleep(3)


def main():
    # 获取页面信息
    html = driver.page_source
    result = etree.HTML(html)
    # 数据列表，用来存储数据并保存为csv文件
    data_list = []
    content_list = result.xpath('//div[@id="listContent"]//div[@class="listItemBox clearfix"]')
    for item in content_list:
        # 工作名称
        job_name = item.xpath('.//div[@class="jobName"]//span/@title')[0]
        # 薪水
        job_saray = item.xpath('.//p[@class="job_saray"]/text()')[0]
        # 工作需求列表
        job_demand_list = item.xpath('.//ul[@class="job_demand"]/li')
        # 工作地点
        job_place = job_demand_list[0].xpath('./text()')[0]
        # 工作经验
        job_experience = job_demand_list[1].xpath('./text()')[0]
        # 学历要求
        try:
            job_cademic = job_demand_list[2].xpath('./text()')[0]
        except:
            job_cademic = ''
        # 公司福利
        job_welfare = ''
        job_welfare_list = item.xpath('.//div[@class="job_welfare"]//div[@class="welfare_item"]')
        for i in job_welfare_list:
            if job_welfare != '':
                job_welfare = job_welfare + '、' + i.xpath('./text()')[0]
            else:
                job_welfare = i.xpath('./text()')[0]

        # 公司名称
        commpanyName = item.xpath('.//div[@class="commpanyName"]//a/text()')[0]
        # 公司描述
        commpanyDesc_list = item.xpath('.//div[@class="commpanyDesc"]//span/text()')
        commpanyDesc = ''
        for i in commpanyDesc_list:
            commpanyDesc = commpanyDesc + i

        data_dict = {'job_name': job_name, 'job_saray': job_saray, 'job_place': job_place,
                     'job_experience': job_experience,
                     'job_cademic': job_cademic, 'job_welfare': job_welfare, 'commpanyName': commpanyName,
                     'commpanyDesc': commpanyDesc}
        # 将数据保存为csv文件
        print(job_name, job_saray, job_place, job_experience, job_cademic, job_welfare, commpanyName, commpanyDesc)
        data_list.append(data_dict)
    save_as_csv(data_list)
    # 点击下一页,获取下一页数据
    try:
        # 判断是否有下一页
        button = result.xpath('//button[@class="btn btn-pager btn-pager-disable"]')
        if len(button) == 1:
            text = button.xpath('./text()')
            if text == '下一页':
                print('程序结束')
            else:
                driver.find_elements_by_xpath('//div[@class="pager"]//button')[1].click()
                main()
                time.sleep(3)
        else:
            print('程序结束')
    except:
        print('程序结束')


def save_as_csv(data_list):
    '''将数据保存为csv文件'''
    csvfile = open('data.csv', 'a')
    fieldnames = ['job_name', 'job_saray', 'job_place', 'job_experience', 'job_cademic', 'job_welfare', 'commpanyName',
                  'commpanyDesc']
    writehandler = csv.DictWriter(csvfile, fieldnames)
    # 写入头
    writehandler.writeheader()
    # 写入数据
    writehandler.writerows(data_list)
    csvfile.close()


if __name__ == '__main__':
    main()
