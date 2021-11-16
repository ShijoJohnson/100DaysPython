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

def evalAmt(drink, totAmt):
    if MENU[drink][cost]<= totAmt:
        return True
    else:
        return False


def askInputs():
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    print(f"Please insert coins.")
    inpQtr = int(input("how many quarters?: "))
    inpDimes = int(input("how many dimes?: "))
    inpNiks = int(input("how many nickles?: "))
    inpPens = int(input("how many pennies?: 1"))
    totAmt = (inpQtr * .25) + (inpDimes*.1) + (inpNiks*.05) + (inpPens*.01)
    drinkReady = evalAmt(drink, totAmt)
    if drinkReady:
        print("Here is your drink")
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


