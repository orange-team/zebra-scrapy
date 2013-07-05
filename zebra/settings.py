# Scrapy settings for zebra project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'zebra'

SPIDER_MODULES = ['zebra.spiders']
NEWSPIDER_MODULE = 'zebra.spiders'

DOWNLOADER_MIDDLEWARES = {
    #'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    # Fix path to this module
    # 'spider.randomproxy.RandomProxy': 100,
    'zebra.proxy_middleware.ProxyMiddleware': 100,
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = './zebra.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zebra (+http://www.yourdomain.com)'
ITEM_PIPELINES = ['zebra.pipelines.ZebraPipeline']


LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = './zebra.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False
