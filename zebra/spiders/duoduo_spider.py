#########################################################################
# File Name: duoduo_spider.py
# Author: altmivip
# mail: altmivip@163.com
#########################################################################
#!/usr/bin/python

#from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from duoduo.items import DuoduoItem

class duoduoSpider(CrawlSpider):
    name = "duoduo"
    allowed_domains = ['duoduo.cn']
    # 知识 > 准备怀孕
    start_urls = [
            "http://www.duoduo.cn/knows,list/101",
            "http://www.duoduo.cn/knows,list/112"
            ]

#    def parse(self,response):
#        hxs = HtmlXPathSelector(response)
#
#        frontNews = hxs.select("//ul[@class='recom_list']/li/p[@class='recom_title']")
#        items = []
#        for site in frontNews:
#            item = ZebraItem()
#            item['title'] = site.select('a/text()').extract()
#            item['link'] = site.select('a/@href').extract()
#            items.append(item)
#        
#        lastNew = hxs.select("//ul[@class='time_list']/li")
#        for site in lastNew:
#            item = ZebraItem()
#            item['title'] = site.select('a/text()').extract()
#            item['link'] = site.select('a/@href').extract()
#            items.append(item)
#
#        return items

    rules = (
#Rule(SgmlLinkExtractor(allow=('nutrition'))),
        Rule(SgmlLinkExtractor(allow=('\/nutrition\/')),callback='parse_item'),
    )

    def parse_item(self,response):
        self.log('page:%s' % response.url)
        hxs = HtmlXPathSelector(response)
        item = ZebraItem()
        item['title'] = hxs.select("//h1/text()").extract()
        item['link'] = response.url
        item['content'] = hxs.select("//div[@class='cont_font114']/*").extract()
        return item

