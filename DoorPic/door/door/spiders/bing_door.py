# -*- coding: utf-8 -*-
import scrapy
from door.items import DoorItem
import json

class BingDoorSpider(scrapy.Spider):
    name = 'bing_door'
    allowed_domains = ['cn.bing.com']
    start_urls = ['http://cn.bing.com/']
    count = 1
    source_url = 'https://cn.bing.com/images/async?q=%E6%9C%A8%E9%97%A8&first={0}&count=35&relp=35&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased&mmasync=1&dgState=x*0_y*0_h*0_c*8_i*71_r*8&IG=E9E30A0EEBAC4E4CB15A192D41887046&SFX=3&iid=images.5639'

    tar_url = source_url.format(count)

    def start_requests(self):
        yield scrapy.Request(self.tar_url, callback=self.get_url)

    def get_url(self, response):
        item = DoorItem()
        source = []
        for i in map(json.loads, response.xpath('//@m').extract()):
            source.append(i['murl'])
        item['image_urls'] = source
        yield item

        self.count +=  35
        print(self.count)
        self.tar_url = self.source_url.format(self.count)
        if self.count < 100:
            yield scrapy.Request(self.tar_url, callback=self.get_url)






