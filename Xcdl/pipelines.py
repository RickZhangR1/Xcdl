# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Xcdl.items import XicispItem
from Xcdl.items import MinhuaItem
from Xcdl.mssqlpipelines import sql

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request



class XcdlPipeline(object):
    def process_item(self, item, spider):
        return item

class XcdlspPipeline(object):
    def process_item(self,item,spider):
        if isinstance(item,XicispItem):
            ip=item['proxy_ip']
            ret=sql.MsSql.select_name(ip)
            if ret==1:
                print(ip,'已经存在了-----')
            else:
                results=(item['proxy_country'],
                         item['proxy_ip'],
                         item['proxy_port'],
                         item['proxy_server_address'],
                         item['proxy_anonymous'],
                         item['proxy_type'],
                         item['proxy_survival_time'],
                         item['proxy_verify_time'],
                        )
                sql.MsSql.insert_db_xcdl(results)
#名画存储中间件
class MinhuaPipelines(ImagesPipeline):
    def get_media_requests(self, item, info):#重写下载图片的方法
        print(item['img_url'],'-------------------------------')
        yield Request(item['img_url'])

    # def process_item(self,item,spider):
    #     if isinstance(item,MinhuaItem):
    #         print(item['img_url'])

