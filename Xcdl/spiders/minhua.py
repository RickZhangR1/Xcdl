# -*- coding: utf-8 -*-
import scrapy
from Xcdl.items import MinhuaItem


class MinhuaSpider(scrapy.Spider):
    name = 'minhua'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html/']

    def parse(self, response):
        #xpath 筛选
        #print(response.xpath('//div[@class="post-content"]/p/img/@src').extract())
        #css筛选
        urls=response.css('.post-content p img::attr(src)').extract()
        print(urls)
        print(len(urls))
        print('-----------------------------------------------------'*3)

        item=MinhuaItem()
        for url in urls:
            item['img_url']=url
            yield  item
