import scrapy
from items import First_scrapyItem

class MyprojectSpider(scrapy.Spider):
   name = "project"
   allowed_domains = ["dmoz.org"]
   
   start_urls = [
      "https://www.lovebonito.com/sg/shop/apparel-accessories/tops", 
      "https://www.lovebonito.com/sg/shop/apparel-accessories/skirts"
   ]
   def parse(self, response):
      for sel in response.xpath('//a/h3'):
         item = First_scrapyItem()
         item['title'] = sel.xpath('/text()').extract()
         item['link'] = sel.xpath('/@href').extract()
         item['desc'] = sel.xpath('text()').extract()
         yield item