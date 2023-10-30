from menu import MENU, resources


# TODO: 3. Print report
def show_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# TODO: 4. Check if resources sufficient
def check_resources(menu_choice, current_resources):
    ingredients_needed = MENU[menu_choice]["ingredients"]
    for ingredient in ingredients_needed:
        if ingredients_needed[ingredient] > current_resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


# TODO: 5. Process coins
def process_coins():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


# TODO: 6. Check transaction successful
def check_transaction(menu_choice, coins):
    price = MENU[menu_choice]["cost"]
    if price > coins:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        print(f"Here is ${round(coins - price, 2)} in change.")
        return price


# TODO: 7. Make coffee

def make_coffee(menu_choice):
    ingredients_needed = MENU[menu_choice]["ingredients"]
    for ingredient in ingredients_needed:
        resources[ingredient] -= ingredients_needed[ingredient]
    print(f"Here is your {menu_choice} ☕ . Enjoy! ")


money = 0
while True:
    # TODO: 1. prompt user by asking "what would you like? (espresso/latte/cappuccino):"
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt
    if choice == "off":
        break
    if choice == "report":
        show_report()
        continue
    if not check_resources(choice, resources):
        continue
    else:
        coins = process_coins()
        price = check_transaction(choice, coins)
        if price == 0:
            continue
        money += price
        make_coffee(choice)
