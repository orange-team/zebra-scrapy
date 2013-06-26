#########################################################################
# File Name: proxy_middleware.py
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
        '223.4.31.172:3128', # 不透明
        '120.203.215.12:80'
    ]
    request.meta['proxy'] = "http://" + proxy_list[3]



