# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SeleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    movie_year = scrapy.Field()
    movie_name = scrapy.Field()
    movie_kinds = scrapy.Field()
    movie_dir = scrapy.Field()
    movie_act = scrapy.Field()
    movie_kinds = scrapy.Field()
    movie_area = scrapy.Field()
    movie_box = scrapy.Field()
    movie_score = scrapy.Field()
    movie_want = scrapy.Field()
