import pyrebase
import json

def find_allergy(food_list, allergy):
    # Initialize Firebase
    allergic_foods = []
    config_file = "config.json"
    with open(config_file) as configfile:
        config = json.load(configfile)
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    foods = db.child("menu").get().val()
    for food in food_list:
        if allergy in foods[food][0]:
            allergic_foods.append(food)
    if len(allergic_foods) == 0:
        print("No foods found")
    if len(allergic_foods) == 1:
        print(f"(!) {allergic_foods[0]} contains {allergy} (!)")
    if len(allergic_foods) > 1:
        print(f"The following foods contain >> {allergy} <<:")
        for food in allergic_foods:
            print(food.title())
        request = input("Would you like to see the ingredients for these foods? (y/n): ")
        if request.lower() == "y":
            for food in allergic_foods:
                print(f"{food.upper()}: \nIngredients: {foods[food][0]}")
        else:
            print("Goodbye")

def search(val):
    val = val.upper()
    found_foods = []
    # Initialize Firebase
    config_file = "config.json"
    with open(config_file) as configfile:
        config = json.load(configfile)
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    foods = db.child("menu").get().val()
    for food in foods.keys():
        if val in food:
            found_foods.append(food)
    return found_foods          

dish = input("Enter a dish: ")
allergy = input("Enter an allergy: ") 

foods = search(dish)
find_allergy(foods, allergy)