from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()

is_on = True




while is_on:

    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        print("Shutting down...")
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                is_payment_made = money_machine.make_payment(drink.cost)
                if is_payment_made:
                    coffee_maker.make_coffee(drink)


