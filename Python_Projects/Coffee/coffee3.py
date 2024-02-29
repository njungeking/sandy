# A third attempt at the virtual coffee machine project.

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
register = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Create a function that determines the available resources for a particular drink.
def checker(drink_components, resources_available):
    for item in drink_components:
        if drink_components[item] > resources_available[item]:
            print(f"Sorry. There is not enough {item} for your order!")
            return False
        else:
            return True

# A function that asks the customer for money.
def billing():
    print("Please deposit some money.")
    total = 0
    total += int(input("How many quarters do you have? ")) * 0.25
    total += int(input("How many dimes do you have? ")) * 0.1
    total += int(input("How many nickels do you have? ")) * 0.05
    total += int(input("How many pennies do you have? ")) * 0.01
    return total


# A function that checks whether the money deposited is enough.
def money_checker(money_received, actual_cost):
    if money_received > actual_cost:
        global register
        register += actual_cost
        bal = round(money_received - actual_cost, 2)
        print(f"Here is your balance: ${bal}")
        return True
    else:
        print(f"Sorry. {money_received} is not enough. You need: {actual_cost}!")
        return False


def final_coffee(drink_ingredients, cof):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Please enjoy your {cof}!")


print("Welcome to a virtual coffee machine!")

run = True
while run:
    order = input("Please place your desired order: (Cappuccino, Latte or Espresso): ").lower()
    if order == "off":
        print("Goodbye! See you next time!")
        run = False
    elif order == "report":
        print(f"Milk remaining: {resources['milk']}ml.")
        print(f"Water remaining: {resources['water']}ml.")
        print(f"Coffee remaining: {resources['coffee']}g.")
        print(f"Register amount balance: ${register}.")
    else:
        #Check if there are sufficient resources for the desired drink.
        drink = MENU[order]
        if checker(drink["ingredients"], resources):
            #Ask the customer for payment.
            payment = billing()
            if money_checker(payment, drink["cost"]):
                # Make the drink and adjust for the resources.
                final_coffee(drink["ingredients"], order)
