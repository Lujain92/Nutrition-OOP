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
# @pytest.mark.skip
# def test_three():
#     recepies=Recepies()
#     recepies.set_query('italian wedding soup')
#     recepies.get_data()
#     actual=recepies.get_ingredients()
#     expected=""
#     assert actual== expected
# @pytest.mark.skip   
# def test_four():
#     recepies=Recepies()
#     recepies.set_query('italian wedding soup')
#     recepies.get_data()
#     actual=recepies.get_instructions()
#     expected=""
#     assert actual== expected    