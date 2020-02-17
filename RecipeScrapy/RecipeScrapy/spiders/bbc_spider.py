import scrapy

class BbcSpider(scrapy.Spider):
    name = 'bbcRecipe'
    recipes = []
    def start_requests(self):
        #url = 'https://www.bbcgoodfood.com/recipes/collection/easy?page=0#c'
        for i in range(4):            
            url = 'https://www.bbcgoodfood.com/recipes/collection/easy?page=%d#c' % i
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):# reposen is the page content
        page = response.url.split("?")[-1]#get the last split element by -1 index
        filename = self.name+'-%s.json' % page
        for r in response.css('article'): #get all the recipe's article
            name = r.css(".teaser-item__title a::text").get()
            imageUrl = r.css(".teaser-item__image a::href").get()
            self.recipes.append(recipeObject(name,imageUrl,ingredients,steps))
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

    def getSteps(self,page):

        return True

    def getIngredients(self,page):

        return True


class recipeObject:    
    def __init__(name,imageUrl,ingredients,steps):
        self.name = name
        self.imageUrl = imageUrl
        self.ingredients = ingredients
        self.steps = steps
