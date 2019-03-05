# -*- coding: utf-8 -*-
import scrapy
from Xcdl.settings import DEFAULT_REQUEST_HEADERS
page=0
class LianjiaspSpider(scrapy.Spider):
    name = 'lianjiasp'
    allowed_domains = ['su.lianjia.com']
    #start_urls = ['https://su.lianjia.com/zufang/pg1']
    #definition url address
    def start_requests(self):
        start_urls=[
            r'https://su.lianjia.com/zufang/pg{0}'.format(i) for i in range(1,3)
        ]
        print(start_urls)
        for start_url in start_urls:
            print(DEFAULT_REQUEST_HEADERS['User-Agent'])
            yield scrapy.Request(url=start_url,callback=self.parse,dont_filter=True,headers=DEFAULT_REQUEST_HEADERS)
    def parse(self, response):
        #global page
        #page+=1
        #print('-----')
        #with open (r'C:\Users\zhangr1\PycharmProjects\Xcdl\Xcdl\html\lianjiapg{}.html'.format(page),'w',encoding='utf-8') as f :
        #    f.write(response.body.decode('utf-8'))
        infos =response.xpath('//div[@class="content__list--item"]')


        for info in infos:
            # image link 图片链接
            print(info)
            img_src=info.xpath('./a/img/@data-src').extract()
            try:
                img_src = img_src[0]
            except:
                img_src = None

            #info_title 房屋信息标题
            title=info.xpath('./div/p[@class="content__list--item--title twoline"]/a/text()').extract()
            try:
                title = title[0]
            except:
                title = None

            #详情链接
            detail_link = info.xpath('./a[@class="content__list--item--aside"]/@href').extract()
            try:
                detail_link = detail_link[0]
                detail_link = 'https://su.lianjia.com' + detail_link
            except:
                detail_link=None
            if detail_link is not None:
                yield scrapy.Request(url=detail_link,callback=self.detail_parse,dont_filter=True,headers=DEFAULT_REQUEST_HEADERS,meta={'img_src':img_src,'title':title,'detail_link':detail_link})
    #详情解析方法
    def detail_parse(self,response):
        global page
        page+=1
        print(response.meta)
        with open(r'C:\Users\zhangr1\PycharmProjects\Xcdl\Xcdl\html\detailpg{}.html'.format(page), 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))
        #print(response.body.decode())
