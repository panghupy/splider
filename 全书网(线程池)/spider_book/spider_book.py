from concurrent.futures import ThreadPoolExecutor
import requests
import threading
from lxml import etree
import os


# 采集数据，进入详情页，获取章节列表和url
def crawl_data(page):
    # 每一页的url
    for i in page:
        page_num = i
    url = 'http://www.quanshuwang.com/list/1_' + str(page_num) + '.html'
    # print(url)
    html = get_html_from_url(url)
    li_list = html.xpath('//ul[contains(@class,"seeWell")]/li')
    # 得到每一个文章的li
    for li in li_list:
        # 得到详情页url,请求详情页，找到点击开始阅读
        print("进入详情页-----------------------")
        detail_url = li.xpath('./a/@href')[0]
        html = get_html_from_url(detail_url)
        read_url = html.xpath('//div[@class="b-oper"]/a/@href')[0]
        print('点击开始阅读---------------------')
        # print(read_url)
        html = get_html_from_url(read_url, 'gbk')
        # 文章标题
        title = html.xpath('//div[@class="chapName"]//strong/text()')[0]
        # print(title)
        # 创建文件夹
        dir = '../' + title
        if not os.path.exists(dir):
            os.mkdir(dir)
        # 章节列表
        chapter_list = html.xpath('//div[@class="chapterNum"]//li')
        for chapter in chapter_list:
            # 章节链接
            chapter_url = chapter.xpath('./a/@href')[0]
            # 章节标题
            chapter_title = chapter.xpath('./a/text()')[0]
            print(chapter_url, chapter_title)

            return chapter_title, chapter_url, title


# 请求一个url，返回html对象
def get_html_from_url(url, code='utf-8'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
    }
    response = requests.get(url, headers=headers)
    response.encoding = code
    response = response.text
    html = etree.HTML(response)
    return html


# 通过分类。得到这种分类的书有多少页
def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
    }
    response = requests.get(url, headers)
    response.encoding = 'gbk'
    response = response.text
    # print(response)
    html = etree.HTML(response)
    page = int(html.xpath('//div[@id="pagelink"]//a[last()]/text()')[0])
    return page


# 解析数据，进入每个章节获取内容，并保存在本地
# 回调函数接收一个结果集
def parse_data(data):
    # data是一个对象，result()方法返回的才是传过来的数据
    chapter_title = data.result()[0]
    chapter_url = data.result()[1]
    title = data.result()[2]
    # 章节内容
    html = get_html_from_url(chapter_url, 'gbk')
    content = ''
    content_list = html.xpath('//div[@class="mainContenr"]/text()')
    for i in content_list:
        content = content + i.replace('\xa0\xa0\xa0\xa0', '\t').replace('\r\n', '\n')
    filename = '../' + title.replace('/', '') + '/' + chapter_title + '.txt'
    # 将文章内容写入到txt文件中
    with open(filename, 'w')as f:
        f.write(content)


def main():
    # 玄幻分类，也就是第一个分类的接口
    url = 'http://www.quanshuwang.com/list/1_1.html'
    page = get_page(url)
    # ThreadPoolExecutor帮我们创建一个线程池)
    # 如何构造一个线程池(里面有是个子线程)
    pool = ThreadPoolExecutor(max_workers=60)
    for i in range(1, page - 1):
        # 执行完毕任务之后返回的结果
        handle = pool.submit(crawl_data, (i,))
        # 回调函数
        handle.add_done_callback(parse_data)


if __name__ == '__main__':
    main()
