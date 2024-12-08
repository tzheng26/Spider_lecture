import scrapy
from scrapy_movie_049.items import ScrapyMovie049Item

class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["btwuji.com"]
    start_urls = ["https://btwuji.com/html/gndy/china/index.html"]

    def parse(self, response):
        # 要第一个的名字和第二页的图片

        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')
        for a in a_list:
            # 获取第一页的name 和 要点击的链接
            name = a.xpath('./text()').extract_first()
            src = a.xpath('./@href').extract_first()
            # print(name, src)

            # 第二页的地址
            url = 'https://btwuji.com' + src
            # print(url)

            # 对第二页的链接发起访问
            yield scrapy.Request(url, callback=self.parse_second, meta={'name': name})


    def parse_second(self, response):
        # 获取第二页的图片

        # 有坑，这里span失败不了，返回的都是None
        # 注意：如果拿不到数据的情况下，一定要检查你的xpath语法是否正确
        # src = response.xpath('//div[@id="Zoom"]/span/img/@src').extract_first()
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        print(src)

        # 接受到请求的那个meta参数的值
        name = response.meta['name']

        movie = ScrapyMovie049Item(src=src, name=name)

        yield movie

