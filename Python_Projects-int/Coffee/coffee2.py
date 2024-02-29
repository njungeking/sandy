# A second attempt at the Coffee Machine Project.

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Create a function that is able to compare the drink requirements against the available resources.


def compare(order):
    """This function returns True or False depending on whether there are enough resources available to make a drink."""
    for item in order:
        if order[item] >= resources[item]:
            print(f"Sorry, there is not enough {item} for your order!")
            return False
    return True

# Create a function that processes the coins entered by the customer.


def coins():
    """This function returns the total amount of money calculated as per the customer's entries."""
    print("Please insert coins.")
    total = int(input("Enter quarters: ")) * 0.25
    total += int(input("Enter dimes: ")) * 0.1
    total += int(input("Enter nickels: ")) * 0.05
    total += int(input("Enter pennies: ")) * 0.01
    return total

# Create a function that checks whether the amount paid is equal to or greater than the drink's cost.


def transaction(money, price):
    if money >= price:
        global profit
        profit += price
        change = round(money - price, 2)
        print(f"Here is your change: ${change}")
        return True
    else:
        print(f"Sorry. ${money} is not enough to purchase your order! You need ${price}!")
        return False

# Create a (makes_coffee) function.
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name}!")


print("Welcome to a virtual coffee machine!")
is_on = True
while is_on:
    choice = input("Please place your order: Cappuccino, Latte or Espresso: ").lower()
    # Put in place a process of turning off the machine.
    if choice == "off":
        is_on = False
    # Get a way to print the report of the available resources.
    elif choice == "report":
        print(f"Water capacity: {resources['water']}ml.")
        print(f"Milk capacity: {resources['milk']}ml.")
        print(f"Coffee capacity: {resources['coffee']}g.")
        print(f"Money balance: ${profit}.")
    else:
        # Get a way to compare the ingredients of a particular drink against the available resources.
        drink = MENU[choice]
        if compare(drink["ingredients"]):
            payment = coins()
            # Check if the payment is equal to the cost of the drink.
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
