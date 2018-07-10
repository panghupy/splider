# 要使用xpath，首先导入lxml库，lxml是一个解析器，它能够解析xml/html文档
from lxml import etree
import requests

# url = 'https://www.readnovel.com/rank/hotsales?pageNum=1'
url = 'https://www.baidu.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
# }
response = requests.get(url)
print(response.status_code)
#1、首先使用etree将获取到的html文本转换成htmldom(文档模型对象)
# nodename：获取所有符合节点名称的节点(标签)
print(etree.HTML(response))