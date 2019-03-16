# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SelePipeline(object):
    def process_item(self, item, spider):
        with open("info001.txt", "a", encoding='gb18030') as file:
            file.write(item["movie_name"] + '@' + item["movie_year"] + '@' + item["movie_area"] + '@' + item["movie_dir"]
                       + '@' + item["movie_act"] + '@' + item["movie_kinds"] + '@' + item["movie_score"] + '@' + item["movie_box"]
                       + '@' + item["movie_want"] + '\n')
        return item
