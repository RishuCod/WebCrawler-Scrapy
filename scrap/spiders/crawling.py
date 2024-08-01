from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ScrapItem

class Crawling(CrawlSpider):
    name="crawler"
    allowed_domains=["toscrape.com"]
    start_urls=["http://books.toscrape.com/"]

    rules=(
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse"),
    )
    
    def parse(self,response):
          items=ScrapItem()
          title= response.css(".product_main h1::text").get()
          price=response.css(".price_color::text").get()
          items["title"]=title
          items["price"]=price
          yield items

#response.css().get/getall()
#scrapy shell url
#response.xpath().extract()
#scrapy crwal crawler -o file_name.json
#response.css(".attr()")
#yield response.follow(url,callback=self.parse)

