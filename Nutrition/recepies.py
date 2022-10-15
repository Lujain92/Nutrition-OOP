import os
import requests
from dotenv import load_dotenv
from nutrition import item
class Recepies:
    '''
    this class hit a API called receipes and take the data regrading the food you enter
    the data are : ingredients, instrcutions, total caloreis
    '''
    def __init__(self):
        self.food=None
        self.r=None
    def set_food(self,food):
        self.food=food
    def get_data(self):
        self.url='https://api.api-ninjas.com/v1/recipe?query={}'.format(self.food)
        self.r=requests.get(self.url, headers={'X-Api-Key': os.getenv("API_KEY")}).json()
        return self.r
    def get_ingredients(self):
        return self.r[0]["ingredients"].split('|')
        

    def get_instructions(self): 
        return self.r[0]["instructions"]   
    def get_caloreis(self):
        list_ingredients=self.get_ingredients()
        total_calories=0
        for one_food in list_ingredients:
            item.set_query(one_food)
            item.get_data()
            total_calories+=int(item.get_calories())
        return total_calories


        
load_dotenv()
recepies=Recepies() 


