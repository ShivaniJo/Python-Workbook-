import scrapy
from ethical_mw import ethical_delay

class SimpleSpider(scrapy.Spider):
    name = "simple"
    start_urls = ['https://example.com']

    def parse(self, response):
        ethical_delay()
        titles = response.css('h1::text').getall()
        print("Scrapy H1 Titles:", titles)
