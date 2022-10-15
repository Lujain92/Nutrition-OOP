from nutrition import Nutrition
def user_interface():
    print('Welcome to Nutrition')
    print("==========================")
    print('Enter the food item you want to search for')
    x= Nutrition()
    query= input()
    x.set_query(query)
    Nutrition.get_data(x)

    option=input('Enter the option you want to search for: \n 1. Calories \n 2. Protein \n 3. Carbohydrates \n 4. Cholesterol \n 5. Fat \nEnter q to exit the program \n')
    while option != 'q' :
        if option == '1':
            print(f"the calories in {query} is : ", Nutrition.get_calories(x))
        elif option == '2':
            print(f"the protein in {query} is : ", Nutrition.get_protein(x))
        elif option == '3':
            print(f"the carbohydrates in {query} is : ", Nutrition.get_carbohydrates(x))
        elif option == '4':
            print(f"the cholesterol in {query} is : ", Nutrition.get_cholesterol(x))
        elif option == '5':
            print(f"the fat in {query} is : ", Nutrition.get_fat(x))
        else:
            print('Invalid option')
        option=input('Enter the Option you want to search for: \n 1. Calories \n 2. Protein \n 3. Carbohydrates \n 4. Cholesterol \n 5. Fat \nEnter q to exit the program \n')
    print('Thank you for using Nutrition')

    # if option=='1':
    #     print(f"the calories in {query} is : ",x.get_calories()) 
    # elif option=='2':
    #     print(f"the protein in {query} is : ",x.get_protein())
    # elif option=='3':
    #     print(f"the carbohydrates in {query} is : ",x.get_carbohydrates())
    # elif option=='4':
    #     print(f"the cholesterol in {query} is : ",x.get_cholesterol())
    # elif option=='5':
    #     print(f"the fat in {query} is : ",x.get_fat())

    # elif option=='q':
    #     print('Thank you for using Nutrition')
    #     exit()  


user_interface()    
