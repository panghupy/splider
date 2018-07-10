import requests

url = 'https://www.zhihu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
}
response = requests.get(url, headers=headers)
print(response.status_code)
