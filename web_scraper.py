from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Crawling_Spider(CrawlSpider):
    name = 'myspider'
    allowed_domains = ['toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item"),
    )

    def parse_item(self, response):
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "availability" : response.css(".availability::text")[1].get().replace("\n","").replace(" ",""),
            "author": response.css(".author::text").get(),
        }

    

