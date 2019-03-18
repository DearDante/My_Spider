# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
import json


class DoorPipeline(object):
    def process_item(self, item, spider):
        dir_path = r'C:\Users\LittleCanLove\Desktop\door_pic'
        file_count = 0

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        for image in item['image_urls']:
            file_name = image.split(r'/')[-1]
            file_path = os.path.join(dir_path, file_name)

            if os.path.exists(file_path): continue


            with open(file_path, 'wb') as img:
                img.write(requests.get(image).content)

        return item