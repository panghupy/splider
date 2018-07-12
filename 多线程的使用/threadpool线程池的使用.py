from concurrent.futures import ThreadPoolExecutor
import requests
import threading
from lxml import etree


# 采集数据
def crawl_data(page):
    print(page)
    # 打印当前线程的名字
    print(threading.current_thread().name)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
    }
    full_url = 'http://blog.jobbole.com/all-posts/' + str(page)
    response = requests.get(full_url, headers=headers)
    response.encoding = 'utf8'
    # 如果请求成功，就将获取到的内容放到data_queue队列中
    if response.status_code == 200:
        print(200)
        return response.text


# 解析数据
def parse_data(data):
    html = etree.HTML(data.result())
    article_div = html.xpath('//div[@class="post-meta"]')
    for item in article_div:
        title = item.xpath('.//a/text()')[0]
        print(title)
        print('下载成功')


# ThreadPoolExecutor帮我们创建一个线程池)

# 如何构造一个线程池(里面有是个子线程)
pool = ThreadPoolExecutor(max_workers=10)
for i in range(1, 30):
    # 执行完毕任务之后返回的结果
    handle = pool.submit(crawl_data, (i,))
    # 回调函数
    handle.add_done_callback(parse_data)
