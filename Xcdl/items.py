# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XcdlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class XicispItem(scrapy.Item):
    proxy_country=scrapy.Field()
    proxy_ip=scrapy.Field()
    proxy_port=scrapy.Field()
    proxy_server_address=scrapy.Field()
    proxy_anonymous=scrapy.Field()
    proxy_type=scrapy.Field()
    proxy_survival_time=scrapy.Field()
    proxy_verify_time=scrapy.Field()

class MinhuaItem(scrapy.Item):
    img_url=scrapy.Field()
