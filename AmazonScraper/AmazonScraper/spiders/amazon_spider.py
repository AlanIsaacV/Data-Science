# -*- coding: utf-8 -*-
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com.mx']
    start_urls = ['https://www.amazon.com.mx/s?k=laptop&rh=n%3A10189669011&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss']

    def parse(self, response):
        pass
