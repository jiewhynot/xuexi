# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiciItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    ip = scrapy.Field()
    port = scrapy.Field()
    address= scrapy.Field()
    type = scrapy.Field()
    protocol = scrapy.Field()
    speed = scrapy.Field()
    time = scrapy.Field()
    alive_time= scrapy.Field()
    verify_time= scrapy.Field()



