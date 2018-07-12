from selenium import webdriver

browser = webdriver.Chrome(executable_path='/home/song/Desktop/chromedriver')
url = 'https://github.com/login'
browser.get(url)
browser.find_element_by_id('login_field').send_keys('15166396925@163.com')
browser.find_element_by_id('password').send_keys('xiaosong@521.')
browser.find_element_by_name('commit').click()
print(type(browser.get_cookies()))
for cookie in browser.get_cookies():
    print(cookie['name'])

