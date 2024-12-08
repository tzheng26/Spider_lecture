import scrapy
from scrapy_dangdang_045.items import ScrapyDangdang045Item

class DangSpider(scrapy.Spider):
    name = "dang"
    # 如果是多页下载的话 那么必须要调整allowed_domains的范围 一般情况下只写域名
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.01.02.00.00.00.html"]

    base_url = "https://category.dangdang.com/pg"
    page = 1

    def parse(self, response):
        # pipelines.py    下载数据
        # items.py``      定义数据结构

        # src = //ul[@id="component_59"]/li//img/@src
        # name = //ul[@id="component_59"]/li//img/@alt
        # price = //ul[@id="component_59"]/li//p[@class="price"]/span[1]/text() # 第一个span
        
        # 所有的selector的对象都可以再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            # 图片有懒加载，这里要用data-original 而不是src（有的是src2）
            src = li.xpath('.//img/@data-original').extract_first()
            # 第一张图片和其他的图片标签属性不一样
            # 第一张图片的src是可以使用的  其他的图片的地址是data-original
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()

            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            print(src, name, price)

            book = ScrapyDangdang045Item(src=src, name=name, price=price)

            # 获取一个book就将book交给pipelines
            yield book
    
        
# 每一页的爬取的业务逻辑都是一样的，所以我们只需要将执行的那个页的请求再次调用parse方法即可
#   https://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
#   https://category.dangdang.com/pg3-cp01.01.02.00.00.00.html

        if self.page < 100:
            self.page += 1
            url = self.base_url + str(self.page) + "-cp01.01.02.00.00.00.html"

            # 怎么取调用parse方法
            # scrapy.Request就是scrapy的get请求
            # url 就是请求地址
            # callback 是你要执行的那个函数，不允许加()
            yield scrapy.Request(url=url, callback=self.parse)