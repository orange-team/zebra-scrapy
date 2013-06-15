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

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zebra (+http://www.yourdomain.com)'
ITEM_PIPELINES = ['zebra.pipelines.ZebraPipeline']
