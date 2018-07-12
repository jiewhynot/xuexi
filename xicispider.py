# -*- coding: utf-8 -*-
import scrapy

from xici.items import XiciItem


class XicispiderSpider(scrapy.Spider):#爬取西刺代理不能用CrawlSpider,页面改写了，无法匹配到url
    name = 'xicispider'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/']
    list1=[]




    def parse(self, response):
        iplist=response.xpath('//table//tr')
        for ip in iplist[1:3]:
            print(type(ip))
            item=XiciItem()
            item['ip']=ip.xpath('./td[2]/text()').extract()[0]
            item['port']=ip.xpath('./td[3]/text()').extract()[0]
            item['address'] =ip.xpath('./td[4]/a[@href]/text()|./td[4]/text()').extract()[0]
            item['type'] =ip.xpath('./td[5]/text()').extract()[0]
            item['protocol']=ip.xpath('./td[6]/text()').extract()[0]
            item['speed']=ip.xpath('./td[7]/div/@title').extract()[0]
            item['alive_time']=ip.xpath('./td[9]/text()').extract()[0]
            item['verify_time']=ip.xpath('./td[10]/text()').extract()[0]
            self.list1.append(item['ip']+":"+item['port'])
            print(self.list1)#将动态ip添加到列表

            yield item

            for i in range(1,5):
                url="http://www.xicidaili.com/nn/"+str(i)
                yield scrapy.Request(url,callback=self.parse)













