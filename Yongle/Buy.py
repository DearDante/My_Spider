import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Buyer(object):
    '''TODO:
        1. 选择场次和价格
        2. 针对非"立即购买"的处理（无票和抢票，拟采用循环探测）
        3. 多线程购票
        4. 微信反馈购票成功
    '''
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.cookie_str = 'route_yl=384d97d66878ff2e1a2401eae97dfa08; __jsluid=a66301b803548f0f62e3ea167623b6e2; products=530483734%5E%E6%96%87%E8%89%BA%E5%B0%8F%E8%AF%9D%E5%89%A7%E3%80%8A%E6%94%B6%E4%BF%A1%E5%BF%AB%E4%B9%90%E3%80%8B; Hm_lvt_0578294a14fae8ac90f4609ae2844eda=1551331738; __ag_cm_=1; ag_fid=X3aSrH5FFYE9ezUF; _ga=GA1.3.1323537532.1551331739; _gid=GA1.3.1320017268.1551331739; SESSION=a868800a-b96a-4392-af76-33ddaeb9621e; Hm_lpvt_0578294a14fae8ac90f4609ae2844eda=1551331797'

    def _add_cookies(self):
        for i in self.cookie_str.split(';'):
            i = i.strip().split('=')
            self.browser.add_cookie({'name': i[0], 'value': i[1]})

    def buy_once(self, url):
        self.browser.get(url)
        self._add_cookies()
        input = self.browser.find_element_by_class_name('btn-now-buy')
        input.click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "orderSure-bom-submit")))
        input2 = self.browser.find_element_by_class_name('orderSure-bom-submit')
        input2.click()


def main():
    buyer = Buyer()
    buyer.buy_once('https://www.228.com.cn/ticket-530483734.html')


if __name__ =='__main__':
    main()