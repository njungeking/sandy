# A recap of the Virtual Coffee Machine Project.

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


def compare(order_ing):
    for item in order_ing:
        if order_ing[item] > resources[item]:
            print(f"Sorry! There isn't enough: {item}!")
            return False
    return True


def pay_up():
    print("Please pay for your beverage.")
    total = 0
    total += int(input("How many Quarters do you have? ")) * 0.25
    total += int(input("How many Dimes do you have? ")) * 0.1
    total += int(input("How many Nickels do you have? ")) * 0.05
    total += int(input("How many Pennies do you have? ")) * 0.01
    return total


def costing(cash, bev_cost):
    if cash >= bev_cost:
        global register
        register += bev_cost
        bal = round(cash - bev_cost, 2)
        print(f"Here is your balance/change: ${bal}")
        return True
    else:
        print(f"Sorry. {cash} is insufficient. You need {bev_cost}"
              " to purchase this drink.")
        return False


def final(order_req,hot_bev):
    for item in order_req:
        resources[item] -= order_req[item]
    print(f"Please enjoy your {hot_bev}. See you again soon!")


print("Welcome to a sample virtual Coffee Machine!")

mac_on = True
while mac_on:
    order = input("Please place your order: (Cappuccino, Espresso or Latte): ").lower()
    if order == "off":
        print("Goodbye! See you Again!")
        mac_on = False
    elif order == "report":
        print(f"Water remaining is: {resources["water"]}mls.")
        print(f"Milk remaining is: {resources["milk"]}mls.")
        print(f"Coffee remaining is: {resources["coffee"]}g.")
        print(f"Cash remaining in the register is ${register}.")
    else:
        bev = MENU[order]
        if compare(bev["ingredients"]):
            payment = pay_up()
            if costing(payment, bev["cost"]):
                final(bev["ingredients"], order)

