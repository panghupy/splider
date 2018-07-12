import requests
import threading
from lxml import etree
import queue

# 自定义线程类



# 采集数据
def crawl_data(page_queue, data_queue):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
    }

    # 这里从page_queue获取对应的页码
    while not page_queue.empty():
        page = page_queue.get()
        full_url = 'http://blog.jobbole.com/all-posts/' + str(page)
        response = requests.get(full_url, headers=headers)
        response.encoding = 'utf8'
        # 如果请求成功，就将获取到的内容放到data_queue队列中
        if response.status_code == 200:
            print(200)
            data_queue.put(response.text)
def parse_data(data_queue):
    # 不为空的时候去取值
    print('调动parse_data()')
    while not data_queue.empty():

        for data in data_queue.get():
            html = etree.HTML(data)
            article_div = html.xpath('//div[@class="post-meta"]')
            print(article_div)
            title = article_div.xpath('.//a/text()')
            print(title)


def main():
    # 创建一个任务队列:里面的参数maxsize表示最大的存储量
    page_queue = queue.Queue(40)
    # http://blog.jobbole.com/all-posts/2/
    for i in range(1, 30):
        page_queue.put(i)
    # 将解析后的数据放在队列中，供后面的解析线程去解析
    data_queue = queue.Queue()

    # 创建线程去下载任务

    crawlThreadName = ['1号', '2号', '3号', '4号']
    thread_list = []
    for threadName in crawlThreadName:
        thread = threading.Thread(target=crawl_data, name=threadName, args=(page_queue,data_queue))
        # 设置线程守护,默认的，一般不用写
        thread.setDaemon(False)
        # 启动线程
        thread.start()
        thread_list.append(thread)
    # 将线程设置为前台线程
    for thread in thread_list:
        thread.join()

    # 创建线程去解析数据
    parseThreadName = ['解析线程1号', '解析线程2号', '解析线程3号', '解析线程4号', ]
    parseThread = []
    for threadname in parseThreadName:
        thread = threading.Thread(target=parse_data, name=threadname, args=(data_queue,))
        thread.start()
        parseThread.append(thread)

    for thread in parseThread:
        thread.join()


if __name__ == '__main__':
    main()
