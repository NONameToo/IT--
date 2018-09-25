# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ItjuziPipeline(object):
    def __init__(self):
        self.filename = open('companys.json', 'w')

    def process_item(self, item, spider):
        data = dict(item)
        self.filename.write(data)



        # 写到本地的文件



    def close_spider(self, spider):
        self.filename.close()

        return item
