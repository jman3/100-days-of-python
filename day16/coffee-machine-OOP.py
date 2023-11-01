from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


end_of_operation = False
coffee_machine = CoffeeMaker()
menu = Menu()
menu_list = menu.get_items()
money_machine = MoneyMachine()

while not end_of_operation:
    answer = input(f"What would you like? ({menu_list}): ")
    if answer == "off":
        end_of_operation = True
    elif answer == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        choice = menu.find_drink(answer)
        if coffee_machine.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_machine.make_coffee(choice)