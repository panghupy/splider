from multiprocessing import Process

# 实现进程间资源共享的管理类
from multiprocessing import Manager
import requests
from lxml import etree
import csv
import os


def main():
    # 构建一个任务队列
    print('go')
    pageQueue = Manager().Queue(200)
    for i in range(1, 200):
        pageQueue.put(i)
    # 构建一个结果队列，存储获取的响应结果
    dataQueue = Manager().Queue()
    # 查看队列是否为空
    print(pageQueue.empty(), dataQueue.empty())

    # 构建进程
    p1 = Process(target=get_data, args=(pageQueue, dataQueue))
    p2 = Process(target=get_data, args=(pageQueue, dataQueue))
    p3 = Process(target=get_data, args=(pageQueue, dataQueue))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    parse1 = Process(target=parse_data, args=(dataQueue,))
    parse2 = Process(target=parse_data, args=(dataQueue,))
    parse3 = Process(target=parse_data, args=(dataQueue,))
    parse1.start()
    parse2.start()
    parse3.start()
    parse1.join()
    parse2.join()
    parse3.join()


# 获取数据
def get_data(pageQueue, dataQueue):
    while not pageQueue.empty():
        page = pageQueue.get()
        url = 'http://www.quanshuwang.com/list/1_' + str(page) + '.html'
        print('进程开始' + str(os.getpid()))
        print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
        }
        response = requests.get(url, headers=headers)
        response.encoding = 'gbk'
        if response.status_code == 200:
            print('请求成功')
            dataQueue.put(response.text)


# 解析数据
def parse_data(data_queue):
    print('解析进程' + str(os.getpid()))
    while not data_queue.empty():
        html = etree.HTML(data_queue.get())
        li_list = html.xpath('//ul[contains(@class,"seeWell")]/li')


if __name__ == '__main__':
    main()
