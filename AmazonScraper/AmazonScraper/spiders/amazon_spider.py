# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonscraperItem

import datetime

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com.mx']
    start_urls = ['https://www.amazon.com.mx/laptop-Laptops-Computadoras-Componentes-y-Accesorios/s?k=laptop&rh=n%3A10189669011']

    custom_settings = {
        'FEED_URI': 'amazon' + datetime.datetime.today().strftime('%m%d') + '.csv',
        'FEED_FORMAT': 'csv',
        'FEED_EXPORTERS': {
            'csv': 'scrapy.exporters.CsvItemExporter',
        },
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def parse(self, response):
        items = AmazonscraperItem()
        all_products = response.css('.sg-col-20-of-28 > .sg-col-inner')

        for product in all_products: 

            items['name'] = product.css('.a-color-base.a-text-normal::text').get()
            items['price_current'] = product.css('.a-price-whole::text').get()
            items['price_original'] = product.css('.a-text-price .a-offscreen::text').get()

            yield items