import scrapy
class JaimersonCorreiaSpider(scrapy.Spider):
    name = 'jaimersoncorreia'
    start_urls = ['http://www.gilenofilho.com.br/']
    
    def parse(self, response):
        self.log('Hello Word!')
        self.log(response.body)