# A first attempt at the coffee machine project.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def checker(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is no enough {item}!")
            return False
    return True


is_on = True
while is_on:
    choice = input("What would you like to take? (espresso,latte or a capuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
    else:
        drink = MENU[choice]
        checker(drink["ingredients"])
