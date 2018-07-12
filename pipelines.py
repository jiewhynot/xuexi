# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
#
#
class XiciPipeline(object):
    def __init__(self):
        host=settings['MONGO_HOST']
        port=settings['MONGO_PORT']
        database=settings['MONGO_DBNAME']
        sheetname=settings['MONGO_SHEETNAME']
        client=pymongo.MongoClient(host=host,port=port)
        db=client[database]
        self.sheet=db[sheetname]
    def process_item(self, item, spider):
        data=dict(item)
        self.sheet.insert(data)
#         return item
# import json
# class XiciPipeline(object):
#     def __init__(self):
#         self.f=open('xici,json','wb')
#     def process_item(self,item,spider):
#         text=json.dumps(dict(item),ensure_ascii=False)+',\n'
#         self.f.write(text.encode('utf-8'))
#     def close_spider(self,spider):
#         self.f.close()




