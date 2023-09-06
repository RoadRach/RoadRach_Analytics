import scrapy  

class firstSpider(scrapy.Spider): 
   name = "first" 
   allowed_domains = ["dmoz.org"] 
   
   start_urls = [ 
      "https://www.lovebonito.com/sg/shop/apparel-accessories/tops", 
      "https://www.lovebonito.com/sg/shop/apparel-accessories/skirts" 
   ]  
   def parse(self, response): 
      filename = response.url.split("/")[-2] + '.html' 
      with open(filename, 'wb') as f: 
         f.write(response.body)