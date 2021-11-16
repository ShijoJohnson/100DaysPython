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


def reduceItems(drink):
    for i in MENU[drink]["ingredients"]:
        resources[i] -= MENU[drink]["ingredients"][i]
        #print(resources[i])


def evalAmt(drink, totAmt, resources):
    resrcsavailable = True
    if MENU[drink]["cost"] >= totAmt:
        print("Not enough money")
        return False, totAmt
    for i in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][i] >= resources[i]:
            print(f"Not enough {i}")
            return False, totAmt
        else:
            return True, totAmt - MENU[drink]["cost"]


def askInputs():
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "report":
        print(f"Water left is {resources['water']}")
        print(f"Milk left is {resources['milk']}")
        print(f"Coffee left is {resources['coffee']}")
        return drink, 0.0
    else:
        print(f"Please insert coins.")
        inpQtr = int(input("how many quarters?: "))
        inpDimes = int(input("how many dimes?: "))
        inpNiks = int(input("how many nickles?: "))
        inpPens = int(input("how many pennies?: "))
        totAmt = (inpQtr * .25) + (inpDimes*.1) + (inpNiks*.05) + (inpPens*.01)
        return (drink, totAmt)


while True:
    drink, totAmt = askInputs()
    if drink != "report":
        drinkReady, retAmt = evalAmt(drink, totAmt, resources)
        retAmt = round(retAmt, 2)
        if drinkReady:
            print(f"Here is your drink ☕, Balance refund: ${retAmt}")
            reduceItems(drink)
        else:
            print(f"Money refunded, ${totAmt}")











# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])








