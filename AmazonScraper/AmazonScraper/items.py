# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price_current = scrapy.Field()
    price_original = scrapy.Field()
    reviews_number = scrapy.Field()
    score = scrapy.Field()
    importation = scrapy.Field()