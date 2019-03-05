# -*- coding: utf-8 -*-
import scrapy
from Xcdl.items import XicispItem


class XicispSpider(scrapy.Spider):
    name = 'xicisp'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):
        with open('html/xicidl.html','w',encoding='utf-8') as f :
            f.write(response.body.decode('utf-8'))
        item1=response.xpath('//tr[@class="odd"]')
        #print(item1)
        item2=response.xpath('//tr[@class=""]')
        #print(item2)
        items=item1+item2
        for item in items:
            infos=XicispItem()
          #  print(item.extract())
            proxy_country=item.xpath('./td[1]/img/@src').extract()
            try:
                proxy_country = proxy_country[0]
            except:
                proxy_country = None

            proxy_ip=item.xpath('./td[2]/text()').extract()
            try:
                proxy_ip=proxy_ip[0]
            except:
                proxy_ip=None

            proxy_port=item.xpath('./td[3]/text()').extract()
            try:
                proxy_port = proxy_port[0]
            except:
                proxy_port = None

            proxy_server_address = item.xpath('./td[4]/text()').extract()
            try:
                proxy_server_address = proxy_server_address[0]
            except:
                proxy_server_address = None

            proxy_anonymous = item.xpath('./td[5]/text()').extract()
            try:
                proxy_anonymous = proxy_anonymous[0]
            except:
                proxy_anonymous = None

            proxy_type = item.xpath('./td[6]/text()').extract()
            try:
                proxy_type = proxy_type[0]
            except:
                proxy_type = None

            proxy_survival_time = item.xpath('./td[7]/text()').extract()
            try:
                proxy_survival_time = proxy_survival_time[0]
            except:
                proxy_survival_time = None

            proxy_verify_time = item.xpath('./td[8]/text()').extract()
            try:
                proxy_verify_time = proxy_verify_time[0]
            except:
                proxy_verify_time = None
            infos['proxy_country'] = proxy_country
            infos['proxy_ip'] =proxy_ip
            infos['proxy_port'] =proxy_port
            infos['proxy_server_address'] =proxy_server_address
            infos['proxy_anonymous'] =proxy_anonymous
            infos['proxy_type'] =proxy_type
            infos['proxy_survival_time'] =proxy_survival_time
            infos['proxy_verify_time'] =proxy_verify_time
            print((proxy_country,proxy_ip,proxy_port,proxy_server_address,proxy_anonymous,proxy_type,proxy_survival_time,proxy_verify_time))
            yield  infos
