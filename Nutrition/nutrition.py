import os
import requests
from dotenv import load_dotenv


class Nutrition:
    '''
    this class hit a API called nutrition and take the data regrading the food you enter
    the data are : caloreis, carbs, protien, fat, and cholestrol
    '''

    def __init__(self):
        self.query= None
        self.r=None
        
    def set_query(self,query):
        self.query=query
    def get_data(self):
        self.url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(self.query)
        self.r = requests.get(self.url, headers={'X-Api-Key': os.getenv("API_KEY")}).json()
        return self.r    
    def get_calories(self):
        cal=self.r[0]['calories']
        return cal    


        
    def get_protein(self):
        return self.r[0]['protein_g']
    def get_carbohydrates(self):
        return self.r[0]['carbohydrates_total_g']
    def get_cholesterol(self):
        return self.r[0]['cholesterol_mg']
    def get_fat(self):
        return self.r[0]['fat_total_g']
load_dotenv()
item= Nutrition()



