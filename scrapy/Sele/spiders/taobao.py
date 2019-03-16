# -*- coding: utf-8 -*-
import scrapy

from scrapy import Request, Spider
from urllib.parse import quote
from Sele.items import SeleItem

import scrapy
from scrapy import signals

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
import time
class TaobaoSpider(Spider):
    name = 'movie'
    allowed_domains = ['movie.mtime.com']
    start_urls = ['http://movie.mtime.com/{}'.format(str(i)) for i in range(10000, 11500)]
    for url in start_urls:
        def parse(self, response):
            #self.driver = webdriver.PhantomJS()
            # 请求

            # time.sleep(2)

            # 获取请求后得到的源码
            #html = self.driver.page_source
            # 关闭浏览器

            item = SeleItem()
            #str = response.text
            #print(str)
            name= response.xpath("//div[@class = 'clearfix']/h1/text()").extract_first()
            year = response.xpath("//p[@class = 'db_year']/a/text()").extract_first()
            kind_list = response.xpath("//div[@class = 'otherbox __r_c_']/a[@property = 'v:genre']/text()").extract()
            kind = ''
            for i in kind_list:
                kind += i
            item["movie_kinds"] = kind
            dir = response.xpath("//dd[@pan='M14_Movie_Overview_BaseInfo']")[0].xpath("./a/"
                                                                                             "text()").extract_first()
            act = response.xpath("//p[@pan='M14_Movie_Overview_Actor_1']/a/text()").extract_first()
            score = response.xpath("//div[@class = 'gradebox __r_c_']/b").xpath("./text()+./sup/text()").extract_first()
            text = response.xpath("//dl[@class = 'g_toplist_01']/dd/ul/li/text()").extract()
            box = ''
            if(text == None):
                box = ' '
            else:
                if(len(text) in [5, 7]):
                    get_box = text[4]
                    box = response.xpath("//dl[@class = 'g_toplist_01']/dd/ul/li/b/text()").extract()[2] + get_box
                elif (len(text) ==4 ):
                    get_box = text[3]
                    box = response.xpath("//dl[@class = 'g_toplist_01']/dd/ul/li/b/text()").extract()[1] + get_box
                elif(len(text) == 2):
                    get_box = text[1]
                    box = response.xpath("//dl[@class = 'g_toplist_01']/dd/ul/li/b/text()").extract_first() + get_box
            want = response.xpath("//span[@id = 'attitudeCountRegion']/text()").extract_first()
            area = response.xpath("//dd[@pan='M14_Movie_Overview_BaseInfo']")[2].xpath("./a/text()").extract_first()
            if(name == None):
                item["movie_name"] = '没名字'
            else:
                item["movie_name"] = name
            if (year == None):
                item["movie_year"] = '没年份'
            else:
                item["movie_year"] = year
            if (dir == None):
                item["movie_dir"] = '没导演'
            else:
                item["movie_dir"] = dir
            if (act == None):
                item["movie_act"] = '没名字'
            else:
                item["movie_act"] = act
            if (score== None):
                item["movie_score"] = '没分数'
            else:
                item["movie_score"] = score
            if (box == ''):
                item["movie_box"] = '没票房'
            else:
                item["movie_box"] = box
            print(item["movie_box"])
            if (want == None):
                item["movie_want"] = '没想看人'
            else:
                item["movie_want"] = want
            if (area == None):
                item["movie_area"] = '没地区'
            else:
                item["movie_area"] = area
            yield item

            # print('name: '+ item["movie_name"])
            # print('year: ' + item["movie_year"])
            # print('area: ' + item["movie_area"])
            # print('act: ' + item["movie_act"])
            # print('dir: ' + item["movie_dir"])
            # print('want: ' + item["movie_want"])
            # print('score: ' + item["movie_score"])
            # print('box: ' + item["movie_box"])
            # print('kinds: ' + item["movie_kinds"])
            # yield item
    # keywords = ['ipad']
    # def start_requests(self):
    #     for keyword in self.settings.get('KEYWORDS'):
    #         for page in range(1, self.settings.get('MAX_PAGE') + 1):
    #             url = self.base_url + quote(keyword)
    #             yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    # for url in start_urls:
    #     def parse(self, response):
    #         item = SeleItem()
    #         item["movie_name"] = response.xpath("//div[@class = 'clearfix']/h1/text()").extract_first()
    #         item["movie_year"] = response.xpath("//p[@class = 'db_year']/a/text()").extract_first()
    #         kind_list = response.xpath("//div[@class = 'otherbox __r_c_']/a[@property = 'v:genre']/text()").extract()
    #         for i in len(kind_list):
    #             item["movie_kinds"] += kind_list[i]
    #         item["movie_dir"] = response.xpath("//dd[@pan='M14_Movie_Overview_BaseInfo']")[0].xpath("./a/"
    #                                                                                         "text()").extract_first()
    #         item["movie_act"] = response.xpath("//p[@pan='M14_Movie_Overview_Actor_1']/a/text()").extract_first()
    #
            # products = response.xpath(
            #     '//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class, "item")]')
            # for product in products:
            #     item = SeleItem()
            #     item['price'] = ''.join(product.xpath('.//div[contains(@class, "price")]//text()').extract()).strip()
            #     item['title'] = ''.join(product.xpath('.//div[contains(@class, "title")]//text()').extract()).strip()
            #     item['shop'] = ''.join(product.xpath('.//div[contains(@class, "shop")]//text()').extract()).strip()
            #     item['image'] = ''.join(
            #         product.xpath('.//div[@class="pic"]//img[contains(@class, "img")]/@data-src').extract()).strip()
            #     item['deal'] = product.xpath('.//div[contains(@class, "deal-cnt")]//text()').extract_first()
            #     item['location'] = product.xpath('.//div[contains(@class, "location")]//text()').extract_first()
            #yield item