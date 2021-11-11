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


def update_input(user_input):
    for ingredient in MENU[user_input]["ingredients"]:
        resources[ingredient] -= MENU[user_input]["ingredients"][ingredient]


def check_resources(user_input):
    for ingredient in MENU[user_input]["ingredients"]:
        if resources[ingredient] < MENU[user_input]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False


def process_coins(money):
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    input_sum = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if input_sum < MENU[coffee_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded")
    else:
        if input_sum > MENU[coffee_choice]["cost"]:
            refund_amt = input_sum - MENU[coffee_choice]["cost"]
            print(f"Here's your ${round(refund_amt, 2)} dollars in change.")


def report(balance, resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${balance}")


off = False
balance = 0
while not off:
    coffee_choice = input("What would you like? ")
    if coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
        status = check_resources(coffee_choice)
        if status == False:
            print("")
        else:
            process_coins(balance)
            update_input(coffee_choice)
            balance += MENU[coffee_choice]["cost"]
    elif coffee_choice == "off":
        off = True
    elif coffee_choice == "report":
        report(balance, resources)
    else:
        off = False
