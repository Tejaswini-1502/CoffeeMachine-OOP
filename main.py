from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu1 = Menu()
coffeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
while is_on:
    reply = input(f"What would you like: {menu1.get_items()} ?")
    if reply == "report":
        coffeMaker.report()
        moneyMachine.report()
    elif reply == "off":
        is_on = False
    else:
        ordered_item = menu1.find_drink(reply)
        if ordered_item is not None:
            # check if the sufficient resources are available
            is_res_suf = coffeMaker.is_resource_sufficient(ordered_item)
            # is resources are availabe , ask the user to insert coins
            if is_res_suf:
                success_payment = moneyMachine.make_payment(ordered_item.cost)
                if success_payment:
                    # if payment is successful, make coffee
                    coffeMaker.make_coffee(ordered_item)

