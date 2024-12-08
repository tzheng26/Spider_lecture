# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdang045Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 通俗的说就是你要下载的数据都有什么

    # 图片
    src = scrapy.Field()
    # 书名
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    pass
