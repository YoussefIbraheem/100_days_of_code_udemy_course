from alive_progress import alive_bar
import time

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

COIN_VALUES = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickels': 0.05,
    'pennies': 0.01
}

MY_WALLET = 100.0

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${MY_WALLET}")

def calculate_ingredients(drink):

    for item in drink['ingredients']:
        if resources[item] < drink['ingredients'][item]:
            return 0
    return drink['cost']

def take_user_payment():
    total = 0
    count_of_quarters = int(input("How many quarters? ") or 0)
    count_of_dimes = int(input("How many dimes? ") or 0)
    count_of_nickels = int(input("How many nickels? ") or 0)
    count_of_pennies = int(input("How many pennies? ") or 0)

    total += COIN_VALUES['quarters'] * count_of_quarters
    total += COIN_VALUES['dimes'] * count_of_dimes
    total += COIN_VALUES['nickels'] * count_of_nickels
    total += COIN_VALUES['pennies'] * count_of_pennies

    if total > MY_WALLET:
        print("Sorry that's not enough money. Money refunded.")
        take_user_payment()

    return total

def process_payment(paid_amount,drink_cost):
    if paid_amount < drink_cost:
        change = -1
    elif paid_amount > drink_cost:
        change = paid_amount - drink_cost
    else:
        change = 0

    return  {
        'paid_amount': paid_amount,
        'change': change,
    }

def deduct_ingredients(drink):
    for item in drink['ingredients']:
        resources[item] -= drink['ingredients'][item]


def shutdown_sequence():
    steps = [
        ("Draining excess water...", 0.05),
        ("Purging steam...", 0.07),
        ("Cleaning coffee residue...", 0.09),
        ("Finalizing shutdown...", 0.1)
    ]

    for step, delay in steps:
        with alive_bar(30, title=step, bar='filling', spinner='dots_waves2') as bar:
            for _ in range(30):
                time.sleep(delay)
                bar()

    print("\nMachine has shut down. Goodbye!")


def coffee_machine():
    global MY_WALLET
    taking_order = True

    while taking_order:
        order_intake = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order_intake in MENU:
            chosen_drink = MENU[order_intake]
            if calculate_ingredients(chosen_drink) != 0:
                payment = take_user_payment()
                drink_cost = calculate_ingredients(chosen_drink)
                payment_process = process_payment(payment,drink_cost)
                if payment_process['change'] > 0:
                    deduct_ingredients(chosen_drink)
                    MY_WALLET -= payment_process['paid_amount']
                    MY_WALLET += payment_process['change']
                    print(f"Here is ${payment_process['change']} in change.")
                elif payment_process['change'] < 0:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    deduct_ingredients(chosen_drink)
                    MY_WALLET -= payment_process['paid_amount']
                    print(f"Here is your {order_intake} ☕ Enjoy!")
                    continue

            else:
                print("Sorry there is not enough resources")
                continue

        elif order_intake == 'report':
            print_report()
            continue
        elif order_intake == 'off':
            shutdown_sequence()
            break
        else:
            print("Invalid input")
            continue

coffee_machine()




