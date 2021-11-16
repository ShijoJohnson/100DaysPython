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
        resources[drink]-= MENU[drink]["ingredients"][i]


def evalAmt(drink, totAmt, resources):
    resrcsavailable = True
    if MENU[drink]["cost"] >= totAmt:
        print("Not enough money")
        return False
    for i in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][i] >= resources[i]:
            print(f"Not enough {i}")
            return False
        else:
            return True


def askInputs():
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    print(f"Please insert coins.")
    inpQtr = int(input("how many quarters?: "))
    inpDimes = int(input("how many dimes?: "))
    inpNiks = int(input("how many nickles?: "))
    inpPens = int(input("how many pennies?: "))
    totAmt = (inpQtr * .25) + (inpDimes*.1) + (inpNiks*.05) + (inpPens*.01)
    return (drink, totAmt)


while True:
    drink, totAmt = askInputs()
    drinkReady = evalAmt(drink, totAmt, resources)
    if drinkReady:
        print("Here is your drink")
        retwater, retmilk, retcoffee = reduceItems(drink)
        print(retwater, retmilk, retcoffee)
        resources['water'] = retwater
        resources['coffee'] = retcoffee
        resources['milk'] = retmilk
    else:
        print("Sorry, Suck it up buttercup")
    



# TODO Ask what you like, espresso, latte capuccino

# TODO accept espresso, latte , capuccino and report

# TODO Ask for coins. verify against cost and return change, If not enough say refunded

# TODO IF acceped say here is your drink and reduce it from the balance

# TODO if report print balance

# def verifyAmount():

# def reducefromBal():

# def reportBalance():


# def printdrink():


