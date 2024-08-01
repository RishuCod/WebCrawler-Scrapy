from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ScrapItem
from scrapy.http import FormRequest


class Crawling(CrawlSpider):
    name="crawler1"
    allowed_domains=["toscrape.com"]
    start_urls=["http://books.toscrape.com/login"]


    def parse(self,response):
        token=response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response,formdata={
                "csrf_token":token,
                "username":"cdcdd",
                "password":"ccedc"
        },callback=self.start_parse)
    

    def start_parse(self,response):
          items=ScrapItem()
          title= response.css(".product_main h1::text").get()
          price=response.css(".price_color::text").get()
          items["title"]=title
          items["price"]=price
          yield items
