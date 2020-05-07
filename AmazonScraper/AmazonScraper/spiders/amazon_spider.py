# -*- coding: utf-8 -*-
import scrapy
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

        'DEPTH_LIMIT' : 10
    }

    items = AmazonscraperItem()

    def parse(self, response):
        product_links = response.css('h2 .a-link-normal.a-text-normal::attr(href)').getall()
        for link in product_links: 
            yield response.follow(link, callback=self.parse_product)

        next_page = response.css('.a-last a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


    def parse_product(self, response):
        specs = {}

        name = response.css('#productTitle::text').get()
        name.replace('     \n', '')
        specs['name'] = name
        
        price_current = response.css('#priceblock_ourprice::text').get()
        price_current = price_current if price_current is not None else None
        specs['price_current'] = price_current

        price_original = response.css('.a-text-strike::text').get()
        price_original = price_original if price_original is not None else None
        specs['price_original'] = price_original

        specs['reviews_number'] = response.css('#acrCustomerReviewText::text').get()
        
        specs['seller'] = response.css('#bylineInfo::text').get()

        specs['score'] = response.css('#acrPopover .a-icon-alt::text').get()


        rows = response.css('.pdTab table tr')
        for row in rows:
            try:
                column = row.css('td::text').getall()
                specs[column[0]] = column[1]
            except IndexError:
                pass
        del specs['Clasificación en los más vendidos de Amazon']

        yield specs
