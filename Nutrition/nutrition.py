from re import X
import requests

class Nutrition:

    def __init__(self):
        self.query= None
        self.r=None
        
    def set_query(self,query):
        self.query=query
    def get_data(self):
        self.url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(self.query)
        self.r = requests.get(self.url, headers={'X-Api-Key': '/F21ZHdQSAnFvWm1wPtgDg==T0gB03ZqMXBWg0ID'}).json()
        return self.r    
    def get_calories(self):
        return self.r[0]['calories']

    def get_protein(self):
        return self.r[0]['protein_g']
    def get_carbohydrates(self):
        return self.r[0]['carbohydrates_total_g']
    def get_cholesterol(self):
        return self.r[0]['cholesterol_mg']
    def get_fat(self):
        return self.r[0]['fat_total_g']

x= Nutrition()
# x.set_query('apple')
# print(x.get_data())
# print(x.get_calories())
# print(x.get_protein())
# print(x.get_carbohydrates())
# print(x.get_cholesterol())
# print(x.get_fat())

