from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

o_menu = Menu()
o_coffee_maker = CoffeeMaker()
o_money_machine = MoneyMachine()
is_on = True
while is_on:
    inp = input(f"What would you like? ({o_menu.get_items()}): ")
    if inp == "off":
        is_on = False
    elif inp == "report":
        print(o_coffee_maker.report())
        print(o_money_machine.report())
    else:
        o_menu_item = o_menu.find_drink(inp)
        if o_coffee_maker.is_resource_sufficient(o_menu_item):
            # quarters = int(input("Enter the number of quarters: "))
            # dimes = int(input("Enter the number of dimes: "))
            # nickels = int(input("Enter the number of nickles: "))
            # pennies = int(input("Enter the number of pennies: "))
            # tot_amount = round(quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01 )
            if o_money_machine.make_payment(o_menu_item.cost): # tot_amount >= o_menu_item.cost:
                o_coffee_maker.make_coffee(o_menu_item)
            else:
                print(f"Not Enough money, Refunded ${tot_amount}")
        else:
            print("Not enough resources...")



