import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    start_urls = ["https://car.autohome.com.cn/price/brand-15.html"]

    def parse(self, response):
        print("================")
