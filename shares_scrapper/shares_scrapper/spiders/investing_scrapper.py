import scrapy

class InvestingScrapper(scrapy.Spider):

    name = 'investing_scrapper'
    allowed_domain = "https://uk.investing.com/equities/united-kingdom"
    start_urls = ["https://uk.investing.com/equities/united-kingdom"]

    def parse(self, response):

        pass
