from selenium import webdriver
import time

chrome_driver = webdriver.Chrome(r"E:\chromedriver_win32\chromedriver.exe")


def register(username, password,driver=chrome_driver):
    # 默认frame
    time.sleep(5)
    # 切换到登录frame
    frame = driver.find_element_by_xpath('//div[@class="login"]/iframe')
    driver.switch_to.frame(frame)

    # 选择账号密码登录
    driver.find_element_by_xpath('//li[@class="account-tab-account"]').click()
    # 用户名输入框
    username_input = driver.find_element_by_xpath('//input[@class="account-form-input"]')
    username_input.clear()
    username_input.send_keys(username)
    time.sleep(2)
    # 密码输入框
    password_input = driver.find_element_by_xpath('//input[@class="account-form-input password"]')
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(1)
    # 登录。
    # 登录按钮的class属性会改变，所以没有使用xpath
    driver.find_element_by_link_text('登录豆瓣').click()
    time.sleep(2)


def goto_movie_list_page(driver=chrome_driver):
    # 定位方法根据导航栏的排列顺序进行定位
    # 可能需要根据豆瓣网页面的变化进行调整
    # 豆瓣 读书 电影 音乐 同城 小组 阅读 FM 时间 豆品 更多
    movie_order = 3
    movie_base_xpath = '//div[@class="global-nav-items"]/ul/li[{}]/a'

    # 从登录后的默认主页跳转至豆瓣电影
    # 打开的新的标签页
    time.sleep(1)
    driver.find_element_by_xpath(movie_base_xpath.format(movie_order)).click()
    # 切换到最新打开的标签页
    driver.switch_to.window(driver.window_handles[-1])

    time.sleep(3)
    # 从豆瓣电影主页跳转到选电影主页
    driver.find_element_by_link_text('选电影').click()
    time.sleep(1)

    time.sleep(2)

    for i in range(10):
        js = "var q=document.documentElement.scrollTop=100000"
        time.sleep(5)
        driver.execute_script(js)
        driver.find_element_by_link_text('加载更多').click()
        time.sleep(7)


def get_profile(filename='config.txt'):
    _profile = {}
    with open(filename, 'r', encoding='utf-8') as fp:
        for line in fp.readlines():
            if line.count('=') == 1:
                k,v = line.split('=')
                _profile[k.strip()] = v.strip()
    return _profile


target_url = 'https://www.douban.com/'

chrome_driver.get(target_url)
chrome_driver.maximize_window()

profile = get_profile()

if profile['username'] and profile['password']:
    register(profile['username'], profile['password'])
    goto_movie_list_page()
else:
    print('找不到配置文件或者配置文件中没有配置登录参数，请确保配置文件中包含指定参数！')



























