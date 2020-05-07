# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonscraperItem

import datetime

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com.mx']
    start_urls = ['https://www.amazon.com.mx/laptop-Laptops-Computadoras-Componentes-y-Accesorios/s?k=laptop&rh=n%3A10189669011']

    custom_settings = {
        'FEED_URI': 'amazon_' + datetime.datetime.today().strftime('%m%d') + '.csv',
        'FEED_FORMAT': 'csv',
        'FEED_EXPORTERS': {
            'csv': 'scrapy.exporters.CsvItemExporter',
        },
        'FEED_EXPORT_ENCODING': 'utf-8',

        'DEPTH_LIMIT' : 2
    }

    items = AmazonscraperItem()

    def parse(self, response):
        product_links = response.css('h2 .a-link-normal.a-text-normal::attr(href)').getall()

        for link in product_links: 
            yield response.follow(link, callback=self.parse_product)

        # next_page = response.css('.a-last a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)


    def parse_product(self, response):
        items = AmazonscraperItem()
        specs = {}

        name = response.css('#productTitle::text').get()
        name.replace('\n', '')
        specs['name'] = name
        
        price_current = response.css('#priceblock_ourprice::text').get()
        price_current = price_current if price_current is not None else None
        specs['price_current'] = price_current

        price_original = response.css('.a-text-strike::text').get()
        price_original = price_original if price_original is not None else None
        specs['price_original'] = price_original

        specs['reviews_number'] = response.css('#acrCustomerReviewText::text').get()
        
        # score = product.css('.a-size-small .a-icon-alt::text').get()
        # score = score.split(' ')[0] if score is not None else None
        # specs['score'] = score

        # importation = False if product.css('.a-color-secondary .s-image').get() is None else True
        # specs['importation'] = importation

        rows = response.css('.pdTab table tr')
        for row in rows:
            try:
                column = row.css('td::text').getall()
                specs[column[0]] = column[1]
            except IndexError:
                pass
        del specs['Clasificación en los más vendidos de Amazon']

        yield specs

        # items['name'] = product.css('.a-color-base.a-text-normal::text').get()

        # price_current_int = product.css('.a-price-whole::text').get()
        # price_current_frac = product.css('.a-price-fraction::text').get()
        # price_current = price_current_int + '.' + price_current_frac if price_current_int is not None else None
        # items['price_current'] = price_current

        # items['price_original'] = product.css('.a-text-price .a-offscreen::text').get()
        # items['reviews_number'] = product.css('.a-size-small .a-size-base::text').get()
        
        # score = product.css('.a-size-small .a-icon-alt::text').get()
        # score = score.split(' ')[0] if score is not None else None
        # items['score'] = score

        # importation = False if product.css('.a-color-secondary .s-image').get() is None else True
        # items['importation'] = importation

        # yield items
