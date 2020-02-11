import scrapy

class BbcSpider(scrapy.Spider):
    name = 'bbcRecipe'

    def start_requests(self):
        url = 'https://www.bbcgoodfood.com/recipes/collection/easy'
        yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        page = response.url.split("/")[-1]
        filename = 'recipe-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)