# 一般情况下，如果网页采用ajax动态加载数据，会返回json数据类型，这时候我们需要将json串转换为python对象
import json
import requests

# json.load():可以将本地文件中的json字符串转换为python对象,写入到本地文件
# json.dump():可以将bendipython字符串转换为json对象,并存储
# json.loads():可以将json字符串转换为python对象
# json.dumps():可以将python字符串转换为json对象

url = 'http://news.baidu.com/widget?id=LocalNews&ajax=json&t=1531118181258'

response = requests.get(url)
result = json.loads(response.text)
# print(result["data"]["LocalNews"]["data"]["rows"])
data = result["data"]["LocalNews"]["data"]["rows"]
pic_news = data['pic']
print(pic_news)