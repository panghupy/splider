import requests

#
# # 发起get请求
url = 'http://news.baidu.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
# }
# # 假如出现ssl错误，说明我们请求的网站使用的是自己创建的证书，也就是使用的未授权的证书,设置verify=Fales就可以忽略未授权的证书
# response = requests.get(url, headers=headers, verify=False)
#
# # 发起post请求
#
# form_data = {
#     'k1': 'v1',
#     'k2': 'v2'
# }
# form_data是参数用来提交表单数据
# response = requests.post('http://httpbin.org/post', form_data)
# print(response.status_code)
# urllib.read()方法返回的是二进制数据
# print(response.text)  # 返回的是解码后的数据
# print(response.content)  # 返回的是二进制码
# print(response.headers)  # 获取响应头
# print(response.headers['server'])  # 获取指定响应头

# 如何使用代理

# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
# }
# proxies = {
#     'scheme': 'ip:port'
# }
#
# response = requests.get(url, headers=headers, proxies=proxies)

# 如何使用cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
}
response = requests.get(url, headers=headers)
print(response.cookies)  # 不完整cookie，返回一个cookiejar对象
print(requests.utils.dict_from_cookiejar(response.cookies))  # 将cookiejar对象转换成字典

# 如何设置一个cookie,将字典传入requests.get()方法里即可
cookies = {
    'BAIDUID': '012826AA5393EF91818B9E45B23FC71D',
    '..': '...',
}

# 如何维持一个会话
# 构造一个session对象来维持会话，他会保存cookie，下次发起请求会携带cookie
session = requests.session()
# 使用session对象发起登录请求
response = session.post('url', 'form_data')
# 登录成功后，再使用session对象发起请求会携带返回的cookies
session.get()

# 上传文件
files ={

}