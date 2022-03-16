MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

go_on = True
deposit = 0
change = 0
money = 0


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check():
    if MENU.get(client_option, {}).get('ingredients').get('water') > resources.get('water'):
        return "No"
    elif MENU.get(client_option, {}).get('ingredients').get('milk') > resources.get('milk'):
        return "No"
    elif MENU.get(client_option, {}).get('ingredients').get('coffee') > resources.get('coffee'):
        return "No"


def coins():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    quarters_add = int(input("How many quarters? "))
    dimes_add = int(input("How many dimes? "))
    nickles_add = int(input("How many nickles? "))
    pennies_add = int(input("How many pennies? "))
    total = (quarters_add * quarters) + (dimes_add * dimes) + (nickles_add * nickles) + (pennies_add * pennies)
    return total


def make_coffee():
    new_water = resources.get('water') - MENU.get(client_option, {}).get('ingredients').get('water')
    new_milk = resources.get('milk') - MENU.get(client_option, {}).get('ingredients').get('milk')
    new_coffee = resources.get('coffee') - MENU.get(client_option, {}).get('ingredients').get('coffee')
    resources['water'] = new_water
    resources['milk'] = new_milk
    resources['coffee'] = new_coffee


while go_on:
    client_option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if client_option == "espresso" or client_option == "latte" or client_option == "cappuccino":
        if client_option == "espresso":
            if check() == "No":
                print("Sorry, we are out of stock\n")
            else:
                print(f"O valor é: ${MENU.get('espresso', {}).get('cost')} ")
                deposit = coins()
                if deposit >= MENU.get('espresso', {}).get('cost'):
                    make_coffee()
                    money += MENU.get('espresso', {}).get('cost')
                    change = deposit - MENU.get('espresso', {}).get('cost')
                    print("Here is your change: {:.2f}".format(change))
                    print("Here is you espresso! Enjoy!\n")
                else:
                    print("Not enough funds, please try again.\n")
        elif client_option == "latte":
            if check() == "No":
                print("Sorry, we are out of stock\n")
            else:
                print(f"O valor é: ${MENU.get('latte', {}).get('cost')} ")
                deposit = coins()
                if deposit >= MENU.get('latte', {}).get('cost'):
                    make_coffee()
                    money += MENU.get('latte', {}).get('cost')
                    change = deposit - MENU.get('latte', {}).get('cost')
                    print("Here is your change: {:.2f}".format(change))
                    print("Here is you Latte! Enjoy!\n")
                else:
                    print("Not enough funds, pleas try again.\n")
        else:
            if check() == "No":
                print("Sorry, we are out of stock\n")
            else:
                print(f"O valor é: ${MENU.get('cappuccino', {}).get('cost')} ")
                deposit = coins()
                if deposit >= MENU.get('cappuccino', {}).get('cost'):
                    make_coffee()
                    money += MENU.get('cappuccino', {}).get('cost')
                    change = deposit - MENU.get('cappuccino', {}).get('cost')
                    print("Here is your change: {:.2f}".format(change))
                    print("Here is your Cappuccino! Enjoy!\n")
                else:
                    print("Not enough funds, pleas try again.\n")
    elif client_option == "off":
        print("The machine is now off.")
        go_on = False
    elif client_option == "report":
        report()
        go_on = False
    else:
        print("Please input a valid option. \n")
