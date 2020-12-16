MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


# TODO 1. Print report of all resources
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    return None


def espresso():
    drink = check_inventory("espresso")
    if drink:
        purchased = purchasing("espresso")
        if purchased:
            print("Transaction successful! Here is your espresso!")
        else:
            print("Insufficient funds. Transaction failed.")
    else:
        print("Insufficient resources available.")
    return None


def cappuccino():
    drink = check_inventory("cappuccino")
    if drink:
        purchased = purchasing("cappuccino")
        if purchased:
            print("Transaction successful! Here is your cappuccino!")
        else:
            print("Insufficient funds. Transaction failed.")
    else:
        print("Insufficient resources available")
    return None


def latte():
    drink = check_inventory("latte")
    if drink:
        purchased = purchasing("latte")
        if purchased:
            print("Transaction successful! Here is your latte!")
        else:
            print("Insufficient funds. Transaction failed.")
    else:
        print("Insufficient resources available")
    return None


def check_inventory(drink):
    new_drink = MENU[drink]
    inventory = False
    while not inventory:
        if new_drink['ingredients']['water'] > resources['water']:
            return inventory
        if new_drink['ingredients']['milk'] > resources['milk']:
            return inventory
        if new_drink['ingredients']['milk'] > resources['milk']:
            return inventory
        else:
            inventory = True
            return inventory


def purchasing(drink):
    transaction = False
    new_drink = MENU[drink]
    total = 0
    change = 0
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))

    quarters_total = quarters * 0.25
    total += quarters_total
    dimes_total = dimes * 0.10
    total += dimes_total
    nickles_total = nickles * 0.05
    total += nickles_total
    pennies_total = pennies * 0.01
    total += pennies_total

    print(total)
    print(new_drink['cost'])

    if new_drink == "espresso":
        if total > new_drink['cost']:
            transaction = True
            change = round(total - new_drink['cost'], 2)
            print(f"${change} refunded as change")
            resources['water'] -= new_drink['ingredients']['water']
            resources['coffee'] -= new_drink['ingredients']['coffee']
            return transaction
        elif total == new_drink['cost']:
            transaction = True
            resources['water'] -= new_drink['ingredients']['water']
            resources['coffee'] -= new_drink['ingredients']['coffee']
            return transaction
        else:
            return transaction

    if total > new_drink['cost']:
        transaction = True
        change = round(total - new_drink['cost'], 2)
        print(f"${change} refunded as change")
        resources['water'] -= new_drink['ingredients']['water']
        resources['milk'] -= new_drink['ingredients']['milk']
        resources['coffee'] -= new_drink['ingredients']['coffee']
        return transaction
    elif total == new_drink['cost']:
        transaction = True
        resources['water'] -= new_drink['ingredients']['water']
        resources['coffee'] -= new_drink['ingredients']['coffee']
        return transaction
    else:
        return transaction


coffeeMachine = True

while coffeeMachine:
    userInput = input("What would you like? (espresso/latte/cappuccino): ")
    if userInput == "espresso":
        espresso()
    elif userInput == "latte":
        latte()
    elif userInput == "cappuccino":
        cappuccino()
    elif userInput == "report":
        report()
    elif userInput == "None":
        coffeeMachine = False
    else:
        print("Invalid command")