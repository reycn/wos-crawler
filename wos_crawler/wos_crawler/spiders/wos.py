import scrapy


class WosSpider(scrapy.Spider):
    name = "wos"
    allowed_domains = ["www-webofscience-com.libproxy1.nus.edu.sg"]
    start_urls = ["https://www-webofscience-com.libproxy1.nus.edu.sg"]
    cookies = {
        
    }
    def parse(self, response):
        pass
