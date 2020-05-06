# -*- coding: utf-8 -*-
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com.mx']
    start_urls = ['https://www.amazon.com.mx/laptop-Laptops-Computadoras-Componentes-y-Accesorios/s?k=laptop&rh=n%3A10189669011']

    def parse(self, response):
        for product in response.css('.sg-col-inner'):

            name = product.css('.a-color-base.a-text-normal::text').get()
            price_current = product.css('.a-price-whole::text').get()
            price_original = product.css('.a-offscreen::text').get()

            yield {
                'name' : name,
                'price_current' : price_current,
                'price_original' : price_original
                }