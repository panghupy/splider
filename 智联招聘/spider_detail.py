import requests
from lxml import etree
from concurrent.futures import ProcessPoolExecutor
import os
import json

# https://fe-api.zhaopin.com/c/i/sou?start=60&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%8A%80%E6%9C%AF&kt=3&lastUrlQuery=%7B%22p%22:2,%22jl%22:%22530%22,%22kw%22:%22%E6%8A%80%E6%9C%AF%22,%22kt%22:%223%22%7D
'''使用多进程爬取智联招聘指定分类100页工作详情信息'''

# 创建进程池
pool = ProcessPoolExecutor()


def get_company_url(start_num):
    print('开启下载任务' + str(os.getpid()))

    url = 'https://fe-api.zhaopin.com/c/i/sou?start=' + str(
        start_num) + '&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%8A%80%E6%9C%AF&kt=3&lastUrlQuery=%7B%22p%22:2,%22jl%22:%22530%22,%22kw%22:%22%E6%8A%80%E6%9C%AF%22,%22kt%22:%223%22%7D'
    response = requests.get(url)
    json_data = response.json()
    # print(response.status_code, response.url)
    # 用json数据找到详情页接口
    detail_url_list = []
    company_name_list = []
    for item in json_data["data"]["results"]:
        # 得到详情页的接口
        detail_url = item["positionURL"]
        with open('detail_url.txt', 'a')as f:
            f.write(detail_url + '\n')
        company_name = item["company"]["name"]
        detail_url_list.append(detail_url)
        # print(company_name)
        company_name_list.append(company_name)
    print('结束下载任务' + str(os.getpid()))
    return detail_url_list, company_name_list


def parse_data(data):
    print('解析任务' + str(os.getpid()))
    detail_url_list = data.result()[0]
    company_name_list = data.result()[1]
    # 把每个工作详情拿出来
    for detail_url in detail_url_list:
        # 判断是否是校园招聘
        if detail_url[-4:] == '.htm':
            print('社会招聘' + detail_url)
            response = requests.get(detail_url).text
            html = etree.HTML(response)
            job_description_list = html.xpath('//ul[@class="terminal-ul clearfix"]/li')
            job_description = ''
            for i in job_description_list:
                print(i.xpath('.//span/text()'))
                if not i.xpath('.//strong/text()'):
                    print(i.xpath('.//strong/text()'))
                else:
                    print(i.xpath('.//strong/a/text()'))
                # job_description = job_description + i.xpath('./text()')
            # print(job_description)


        else:
            print('校园招聘' + detail_url)
    print('结束任务' + str(os.getpid()))


def main():
    print('开启主进程' + str(os.getpid()))
    start_num_list = []
    for i in range(0, 3):
        start_num_list.append(i * 60)

    for start_num in start_num_list:
        handler = pool.submit(get_company_url, start_num)
        handler.add_done_callback(parse_data)
    print('结束主进程' + str(os.getpid()))


if __name__ == '__main__':
    main()
