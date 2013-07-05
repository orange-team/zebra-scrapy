#!/usr/bin/python
#########################################################################
# File Name: yaolan_baike_spider.py
# Author: altmivip
# mail: altmivip@163.com
#########################################################################

#from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from yaolan_baike.items import yaolan_baikeItem

class yaolan_baikeSpider(CrawlSpider):
    name = "yaolan_baike"
    allowed_domains = ['www.yaolan.com']
    start_urls = [
            "http://www.yaolan.com/zhishi/abc.shtml",
            ]

    //接下来抓取对应链接的文章内容
    def parse(self,response):
        hxs = HtmlXPathSelector(response)

        txt_all = hxs.select("//div[@id='list_key']//div[@class='key_time']//dd/a")
        items = []
        for txt in txt_all:
            item = ZebraItem()
            item['baike'] = txt.extract()
            items.append(item)
        return items

