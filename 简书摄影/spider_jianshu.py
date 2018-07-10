import requests
import os
from lxml import etree

# 爬取简书摄影分类
url = 'https://www.jianshu.com/c/7b2be866f564?utm_medium=index-collections&utm_source=desktop'
# 更多内容使用的是ajax请求数据
# https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=2
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
with open('index.html', 'w') as f:
    f.write(response.text)
print(response.status_code)
result = etree.HTML(response.text)
result = result.xpath('//ul[@class="note-list"]/li')
# 获取每个li标签下的东西
for item in result:
    title = item.xpath('.//div[@class="content"]/a/text()')[0]
    url = 'https://www.jianshu.com' + item.xpath('.//div[@class="content"]/a/@href')[0]
    print(title, url)
    # 在这里创建一个以标题命名的文件夹
    if not os.path.exists(title):
        os.mkdir(title)

    # 请求每篇文章的内容，也就是详情页
    response = requests.get(url, headers=headers).text
    with open('detail.html', 'w') as f:
        f.write(response)
    result = etree.HTML(response)
    article_div = result.xpath('//div[@class="article"]')[0]
    # 获取到作者信息的div
    author_div = article_div.xpath('.//div[@class="author"]')[0]
    # 作者姓名
    author_name = author_div.xpath('.//span[@class="name"]/a/text()')[0]
    # 发布时间
    publish_time = author_div.xpath('.//span[@class="publish-time"]/text()')[0]
    # 获取到内容的div
    content_div = result.xpath('//div[@class="show-content"]')[0]
    # 这是一个文本内容列表，里面分别是每一段的内容
    content_text = content_div.xpath('.//p/text()')
    content_p = '标题:'+title+'\n'+'作者:'+author_name+'\n'+'发布时间:'+publish_time+'\n'+'内容:'
    for content in content_text:
        content_p = content_p + '\n' + content
    print(content_p)
    # 将文本内容写入到以标题命名的文件里
    filename = title + '/' + title + '.txt'
    with open(filename, 'w') as f:
        f.write(content_p)

    # 获取文章图片列表
    image_list = content_div.xpath('//img/@data-original-src')
    for image in image_list:
        image_url = 'https:' + image
        print(image_url)
        # 根据图片地址请求图片
        response = requests.get(image_url, headers=headers)
        print('请求图片:' + str(response.status_code))
        filename = title + '/' + image[-10:]
        with open(filename, 'wb') as f:
            f.write(response.content)
