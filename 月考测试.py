from urllib import request,parse,error,robotparser
import requests
import re
import os
url = 'https://www.baidu.com'

r = requests.get(url)

string = 'hello 123456 789'
res = re.search(r'\d+',string)
print(res.group())

for i in range(5,0,-1):
    print(i)