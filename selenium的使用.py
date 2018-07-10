# selenium是一个自动化测试工具
# 应用场景适合在网站使用动态加载的技术(javascript,ajax)
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time
# 有见面浏览器相关设置
# 调用Chrome浏览器创建浏览器对像(指定一下位置)
driver = webdriver.Chrome(executable_path='/home/song/Desktop/chromedriver')
# 打开浏览器，模拟浏览器请求页面
driver.get('https://cn.bing.com/')
# 获取页面信息
html = driver.page_source
# 向必应搜索框中键入关键字
driver.find_element_by_id('sb_form_q').send_keys('surface')
# 点击搜索
driver.find_element_by_id('sb_form_go').click()
time.sleep(3)
driver.back()
driver.close()

# 无界面浏览器相关设置
# 创建chrome参数对象

opt = webdriver.ChromeOptions()
# 把chrome设置成为无界面模式
opt.set_headless()

# 创建chrome无界面对象
driver = webdriver.Chrome(options=opt, executable_path='/home/song/Desktop/chromedriver')
driver.get('https://www.baidu.com')
driver.save_screenshot('1.png')