# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import json
import MySQLdb as mdb
import time

class ZebraPipeline(object):
    def process_item(self, item, spider):
        conn = mdb.connect(host="localhost",user="root",passwd="",db="mydb",port=3307)
        with conn:
            try:
                hde = conn.cursor()
                cuTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                title = mdb.escape_string(item['title'][0].encode('utf8'))
                content = mdb.escape_string(item['content'][0].encode('utf8'))

                sqlOne = "INSERT INTO a_article VALUES(null,'%s','','%s','%s','%s','%s','%s','%s')" %(title,item['source'],cuTime,content,item['section'],item['keyword'],item['link'])
                hde.execute("set names utf8")
                hde.execute(sqlOne)
            except mdb.Error,e:
                print "Error %d: %s" %(e.args[0],e.args[1])
        return item
