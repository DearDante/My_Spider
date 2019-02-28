import requests
from bs4 import BeautifulSoup

class Show(object):
    '''TODO:
        1. 添加剧目信息
        2. 存入数据库
        3. 数据库更新时，微信通知（有新节目时微信通知）
    '''
    def __init__(self, city='', name=''):
        if city == '':
            self.base_url = 'https://www.228.com.cn/s/{0}'.format(name)
        else:
            self.base_url = 'https://www.228.com.cn/s/{0}-{1}'.format(city, name)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }

    def get_10(self, url, target=''):
        r = requests.get(url, headers = self.headers)
        shows = r.json()['products']
        for i in shows:
            show_id = i['productid']
            url = 'https://www.228.com.cn/ticket-{0}.html'.format(show_id)
            if self._find_target(url, target): print(url, i['name'])

    def _get_show_detail_info(self, url):
        r = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(r.content)
        try:
            return soup.select('#productIntroduction ')[0].text
        except IndexError:
            print(url)
            return False

    def _find_target(self, url, target):
        if target == '': return True
        info = self._get_show_detail_info(url)
        if isinstance(info, str):
            if target in info:
                return True
            else:
                return False
        else: return False

    def find_show(self, target=''):
        p = 1
        count = 1
        while(True):
            url = self.base_url+'/?j=1&p={0}'.format(p)
            if len(requests.get(url, headers = self.headers).json()['products']) == 0: break
            else:
                print(count)
                self.get_10(url, target=target)
                p += 1
                count += 10


def main():
    s = Show(name='')
    s.find_show('路飞')
    #s.get_10('https://www.228.com.cn/s/sh-%E4%BF%A1/?j=1&p=1')
    #s.get_show_detail_info('https://www.228.com.cn/ticket-531713073.html')


if __name__ == '__main__':
    main()