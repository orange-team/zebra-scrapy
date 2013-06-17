#########################################################################
# File Name: middlewares.py
# Author: altmivip
# mail: altmivip@163.com
#########################################################################
#!/usr/bin/python
# Importing base64 library because we'll need it ONLY
#in case if the proxy we are going to use requires authentication
import base64

# Start your middleware class
class ProxyMiddleware(object):
  # overwrite process request
  def process_request(self, request, spider):
    # Set the location of the proxy
    proxy_list = [
        '122.49.30.9:80', 
        '125.39.66.147:80', 
        '202.99.172.165:8081',
        '223.4.31.172:3128', # ²»Í¸Ã÷
        '120.203.215.12:80'
    ]
    request.meta['proxy'] = "http://" + proxy_list[3]

# You can use this middleware to have a random user agent every request the spider makes.
# You can define a user USER_AGEN_LIST in your settings and the spider will chose a random user agent from that list every time.
# 
# You will have to disable the default user agent middleware and add this to your settings file.
# 
#     DOWNLOADER_MIDDLEWARES = {
#         'scraper.random_user_agent.RandomUserAgentMiddleware': 400,
#         'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#     }

from scraper.settings import USER_AGENT_LIST
import random
from scrapy import log

class RandomUserAgentMiddleware(object):
    
    def process_request(self, request, spider):
        ua  = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)
        #log.msg('>>>> UA %s'%request.headers)

# Snippet imported from snippets.scrapy.org (which no longer works)
# author: dushyant
# date  : Sep 16, 2011

