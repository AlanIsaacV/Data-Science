# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonscraperItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com.mx']
    start_urls = ['https://www.amazon.com.mx/laptop-Laptops-Computadoras-Componentes-y-Accesorios/s?k=laptop&rh=n%3A10189669011']

    def parse(self, response):
        items = AmazonscraperItem()
        all_products = response.css('.sg-col-20-of-28 > .sg-col-inner')

        for product in all_products: 

            items['name'] = product.css('.a-color-base.a-text-normal::text').get()
            items['price_current'] = product.css('.a-price-whole::text').get()
            items['price_original'] = product.css('.a-offscreen::text').get()

            yield items