from selenium import webdriver
import time

chrome_driver = webdriver.Chrome(r"E:\chromedriver_win32\chromedriver.exe")
target_url = 'https://www.douban.com/'

# 改为自己的
user_name = '********'
password = '********'


def register(url, driver=chrome_driver):
    # 默认frame
    driver.get(url)
    time.sleep(5)
    # 切换到登录frame
    iframe = driver.find_element_by_xpath('//div[@class="login"]/iframe')
    driver.switch_to.frame(iframe)

    # 选择账号密码登录
    driver.find_element_by_xpath('//li[@class="account-tab-account"]').click()
    # 用户名输入框
    username_input = driver.find_element_by_xpath('//input[@class="account-form-input"]')
    username_input.clear()
    username_input.send_keys(user_name)
    time.sleep(2)
    # 密码输入框
    password_input = driver.find_element_by_xpath('//input[@class="account-form-input password"]')
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(1)
    # 登录。
    # 登录按钮的class属性会改变，所以没有使用xpath
    driver.find_element_by_link_text('登录豆瓣').click()

register(target_url)











