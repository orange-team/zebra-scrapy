#########################################################################
# File Name: altmi_spider.py
# Author: altmivip
# mail: altmivip@163.com
#########################################################################
#!/usr/bin/python

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from zebra.items import ZebraItem

class DuoduoSpider(CrawlSpider):
    name = "altmi"
    allowed_domains = ['gz.altmi.com']
    start_urls = [
            "http://gz.altmi.com/proxy_detect.php",
            ]

    def parse(self,response):
       open('test.html', 'wb').write(response.body)
       # self.log('page:%s' % response.url)
       # hxs = HtmlXPathSelector(response)
       # item = ZebraItem()
       # item['title'] = 'test for proxy'
       # item['link'] = response.url
       # item['content'] = hxs.select("//body/*").extract()
       # print title, link, content
       # return item

