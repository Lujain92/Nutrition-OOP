from nutrition import item
from recepies import recepies

def welcome():
    print(""" Welcome to our app that help you to be healthy 
    by let you have an access of a lot of food and the data
    regarding carb,protien,fat content and the caloreis 
    and you can put any recepies you want and we will give you an instrcutrion,
     ingredients and the caloreis for this recepie
    """)
    print("========================================")
    choose=input("""
    if you want to know data about specific food press 1
    if you want to put a type of food and give you how to make press 2
    """)
    if choose == "1":
        return data_of_food()
    elif choose=="2":
        return how_to_make_food()
    else:
        "please choose 1 or 2"

def data_of_food():
    '''
    app that help you to be healthy 
    by let you have an access of a lot of food and the data
    regarding carb,protien,fat content and the caloreis 
    
    '''
    
    food=input("Enter the food item you want to search for\n")
    gram=input("Enter how many gram you want\n")
   
    
    

    item.set_query(f"{gram} of {food}")
    item.get_data()
    try:
        option=input('Enter the option you want to search for: \n 1. Calories \n 2. Protein \n 3. Carbohydrates \n 4. Cholesterol \n 5. Fat \n 6.all\nEnter q to exit the program \n')
        while option != 'q' :
            if option == '1':
                print(f"the calories in {gram} of {food}is : ",item.get_calories())
            elif option == '2':
                print(f"the protein in  {gram} of {food} is : ", item.get_protein())
            elif option == '3':
                print(f"the carbohydrates in  {gram} of {food} is : ", item.get_carbohydrates())
            elif option == '4':
                print(f"the cholesterol in  {gram} of {food} is : ",item.get_cholesterol())
            elif option == '5':
                print(f"the fat in {gram} of {food}is : ", item.get_fat())
            elif option== "6":
                print(f"{gram} of {food} contain {item.get_calories()}  calories and {item.get_protein()} of protein and {item.get_carbohydrates()} of carbohydrate and {item.get_fat()} of fat and {item.get_cholesterol()} of cholerstrol")

            else:
                 print('Invalid option')
            option=input('Enter the option you want to search for: \n 1. Calories \n 2. Protein \n 3. Carbohydrates \n 4. Cholesterol \n 5. Fat \n 6.all\nEnter q to exit the program \n')
        print('Thank you for using Nutrition')

    except:
        print("we don't have this food")


def how_to_make_food():
    '''put any recepies you want and we will give you an instrcutrion,
     ingredients and the caloreis for this recepie'''
    food=input("enter your food that you want to know how to make it\n")
    recepies.set_food(food)
    recepies.get_data()
    try:
        option=input("Enter the option you want to search for: \n 1.Instructions \n 2. Ingredients \n 3. Calories\n 4.all\n Enter q to exit the program \n ")
        while option !='q':
            if option=="1":
                print(f"The instrcution is {recepies.get_instructions()}")
            elif option=="2":
                print("the ingredients are ")
                for ingredient in recepies.get_ingredients():
                    print(ingredient)
                
            elif option=="3":
                print(f"The calories is {recepies.get_caloreis()}")
            elif option=='4':
                print(f'''The instrcution is {recepies.get_instructions()}
                and the calories is {recepies.get_caloreis()}
                and the ingredients are 
                ''')    
                for ingredient in recepies.get_ingredients():
                    print(ingredient)
            else:
                 print('Invalid option')


            option=input("Enter the option you want to search for: \n 1.Instructions \n 2. Ingredients \n 3. Calories\n 4.all\n Enter q to exit the program \n ")



    except:
        print("we don't have this food")

        

          
welcome()
    
