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


def is_amt_enough(drink, amt):
    if amt >= drink["cost"]:
        return True
    else:
        return False


def if_enough_ingredients(drink):
    for _ in drink["ingredients"]:
        if resources[_] < drink["ingredients"][_]:
            print(f"Not enough {_}")
            return False
    return True


is_on = True


def make_coffee(drink):
    for _ in drink["ingredients"]:
        resources[_] -= drink["ingredients"][_]


while is_on:
    inp = input("What would you like? (espresso/latte/cappuccino): ")
    if inp == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"milk: {resources['coffee']}")
    else:
        drink = MENU[inp]
        print("Enter the number of coins")
        quarters = int(input("No of quarters"))
        pennies = int(input("No of pennies"))
        nickels = int(input("No of nickels"))
        dimes = int(input("No of dimes"))
        amt = quarters * 0.25 + pennies * 0.01 + nickels * 0.05 + dimes * 0.1
        transaction_successful = is_amt_enough(drink, amt)
        if transaction_successful:
            if if_enough_ingredients(drink):
                print("Here is your drink")
                make_coffee(drink)
            else:
                print(f"Amount refunded ${amt}")
                cont = input("Continue?? y or n")
                if cont == "n":
                    is_on = False
        else:
            print(f"Sorry Not enough money.., Amount refunded ${amt}")
            cont = input("Continue?? y or n")
            if cont == "n":
                is_on = False


