#########################################################################
# File Name: duoduo_spider.py
# Author: altmivip
# mail: altmivip@163.com
#########################################################################
#!/usr/bin/python

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from zebra.items import ZebraItem

class duoduoSpider(CrawlSpider):
    name = "duoduo"
    allowed_domains = ['duoduo.cn']
    start_urls = [
            "http://www.duoduo.cn/knows,list/101",
            #"http://www.duoduo.cn/knows,list/112"
            ]

    rules = (
        Rule(SgmlLinkExtractor(allow=('\/knows\/')),callback='parse_item'),
    )

    def parse_item(self,response):
        self.log('page:%s' % response.url)
        hxs = HtmlXPathSelector(response)
        item = ZebraItem()
        item['title'] = hxs.select("//h1[@class='hdl']/text()").extract()
        item['link'] = response.url
        item['content'] = hxs.select("//div[@class='content']/*").extract()
        return item

