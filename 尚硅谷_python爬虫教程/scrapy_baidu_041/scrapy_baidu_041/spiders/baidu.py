import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 一般用于运行爬虫的时候使用的值
    name = "baidu"
    # 运行访问的域名列表
    allowed_domains = ["www.baidu.com"]

    # 起始的url地址 指的是第一次要访问的域名
    # start_urls 是在allowed_domains的前面添加一个http://
    #               在allowed_domains的后面添加一个/
    start_urls = ["http://www.baidu.com"]

    def parse(self, response):
        print("苍茫的天涯是我的爱")
