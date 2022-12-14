from Nutrition.nutrition import Nutrition
#from Nutrition.recepies import Recepies
import pytest
def test_one():
    item=Nutrition()
    item.set_query('pizza')
    item.get_data()
    actual=item.get_calories()
    expected=262.9
    assert actual== expected

def test_two():
    item=Nutrition()
    item.set_query('pizza')
    actual=item.get_data()
    expected=[
  {
    "name": "pizza",
    "calories": 262.9,
    "serving_size_g": 100,
    "fat_total_g": 9.8,
    "fat_saturated_g": 4.5,
    "protein_g": 11.4,
    "sodium_mg": 587,
    "potassium_mg": 217,
    "cholesterol_mg": 16,
    "carbohydrates_total_g": 32.9,
    "fiber_g": 2.3,
    "sugar_g": 3.6
  }
]
    assert actual== expected
def test_three():
    item=Nutrition()
    item.set_query('pizza')
    item.get_data()
    actual=item.get_protein()
    expected=11.4
    assert actual== expected

def test_four():
    item=Nutrition()
    item.set_query('pizza')
    item.get_data()
    actual=item.get_carbohydrates()
    expected=32.9
    assert actual== expected

def test_five():
    item=Nutrition()
    item.set_query('pizza')
    item.get_data()
    actual=item.get_cholesterol()
    expected=16
    assert actual== expected

def test_six():
    item=Nutrition()
    item.set_query('pizza')
    item.get_data()
    actual=item.get_fat()
    expected=9.8
    assert actual== expected

  
# @pytest.mark.skip
# def test_seven():
#     recepies=Recepies()
#     recepies.set_query('italian wedding soup')
#     recepies.get_data()
#     actual=recepies.get_ingredients()
#     expected=""
#     assert actual== expected
# @pytest.mark.skip   
# def test_eight():
#     recepies=Recepies()
#     recepies.set_query('italian wedding soup')
#     recepies.get_data()
#     actual=recepies.get_instructions()
#     expected=""
#     assert actual== expected    
# @pytest.mark.skip
def test_nine():
    item=Nutrition()
    item.set_query('fries')
    item.get_data()
    actual=item.get_data()
    expected=[
       {
    "name": "fries",
    "calories": 317.7,
    "serving_size_g": 100,
    "fat_total_g": 14.8,
    "fat_saturated_g": 2.3,
    "protein_g": 3.4,
    "sodium_mg": 212,
    "potassium_mg": 124,
    "cholesterol_mg": 0,
    "carbohydrates_total_g": 41.1,
    "fiber_g": 3.8,
    "sugar_g": 0.3
  }
    ]
    assert actual== expected
def test_ten():
    item=Nutrition()
    item.set_query('fries')
    item.get_data()
    actual=item.get_calories()
    expected=317.7
    assert actual== expected
  
def test_eleven():
    item=Nutrition()
    item.set_query('fries')
    item.get_data()
    actual=item.get_protein()
    expected=3.4
    assert actual== expected
    