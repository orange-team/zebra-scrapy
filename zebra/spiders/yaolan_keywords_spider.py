#!/usr/bin/python
#########################################################################
# File Name: yaolan_keywords_spider.py
# Author: altmivip
# mail: altmivip@163.com
#########################################################################

#from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from yaolan_keywords.items import yaolan_keywordsItem

class yaolan_keywordsSpider(CrawlSpider):
    name = "yaolan_keywords"
    allowed_domains = ['www.yaolan.com']
    start_urls = [
            "http://www.yaolan.com/tag/all/",
            "http://www.yaolan.com/tag/all/2",
            "http://www.yaolan.com/tag/all/3",
            "http://www.yaolan.com/tag/all/4",
            "http://www.yaolan.com/tag/all/5",
            "http://www.yaolan.com/tag/all/6",
            "http://www.yaolan.com/tag/all/7",
            "http://www.yaolan.com/tag/all/8",
            "http://www.yaolan.com/tag/all/9",
            ]

    def parse(self,response):
        hxs = HtmlXPathSelector(response)

        txt_all = hxs.select("//ul[@class='Key_nav1']/a")
        items = []
        for txt in txt_all:
            item = ZebraItem()
            item['keywords'] = txt.extract()
            items.append(item)
        return items

