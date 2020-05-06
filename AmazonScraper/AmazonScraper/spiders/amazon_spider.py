# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonscraperItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com.mx']
    start_urls = ['https://www.amazon.com.mx/laptop-Laptops-Computadoras-Componentes-y-Accesorios/s?k=laptop&rh=n%3A10189669011']

    def parse(self, response):
        items = AmazonscraperItem()

        for product in response.css('.sg-col-inner'):

            items['name'] = product.css('.a-color-base.a-text-normal::text').get()
            items['price_current'] = product.css('.a-price-whole::text').get()
            items['price_original'] = product.css('.a-offscreen::text').get()

            yield items