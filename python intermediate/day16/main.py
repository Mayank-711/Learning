from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
on = True
while on == True:
    print(menu.get_items())
    order = input("Your order:")
    if order == "report":
        print(coffee.report())
    elif order == "off":
        on = False
    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)

