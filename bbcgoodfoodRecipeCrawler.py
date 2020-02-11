# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#library
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

#class and function definition
def getIngredients(pageSoup):
    ingredList = []
    for ingred in pageSoup.select('.ingredients-list__item'):
        ingredList.append(ingred.text)
    return ingredList    

def getSteps(pageSoup):
    stepList = []
    for steps in pageSoup.select('.method__list li p'):
        stepList.append(steps.text)
    return stepList

class recipeObject:
    def __init__(self,recipeName,ingredients,steps):
        self.recipeName = recipeName
        self.ingredients = ingredients
        self.steps = steps;
        
#main class to run
url = 'https://www.bbcgoodfood.com/recipes/collection/easy'
domain = 'https://www.bbcgoodfood.com'
counter = 1
recipeList = []
#req = requests.get(url)
#print(req.text)
driver = webdriver.PhantomJS(executable_path='C:\\Users\\jpkhuang\\Desktop\\installer\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs')
driver.get(url)
# get the home page of the page of the recipe page
print(driver.current_url)
page = driver.page_source
#process html with BeautifulSoup
soup = BeautifulSoup(page,'lxml')
for recipe in soup.select('{}'.format('article .node-recipe')):
    #get the dish name
    recipeName = recipe.select('.teaser-item__title')[0].text
    print('---------'+str(counter)+' '+recipeName+' Start--------------')
    print();
    #get the url link to redirect to the recipe page
    recipeUrl = domain+recipe.select('.teaser-item__image > a')[0]['href']    
    print('Loading url: %s',recipeUrl)
    driver.get(recipeUrl)
    pageSoup = BeautifulSoup(driver.page_source,'lxml')    
    #pushrecipe
    print('push recipe into list...')
    recipeList.append(recipeObject(recipeName,getIngredients(pageSoup),getSteps(pageSoup)))
    print('---------'+str(counter)+' '+recipeName+' end ---------')
    counter+=1


driver.close()
print(recipeList[24])
print('\n---------Recipe crawler end---------')


        
        