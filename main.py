MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 130,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 160,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 180,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0,
}
USER = {
    "change": 0,
}


def transaction(action):
    money = int(input("Enter the amount: "))
    if action == "espresso":
        if money >= MENU[action]["cost"]:
            USER["change"] = money - MENU[action]["cost"]
            resources["Money"] += MENU[action]["cost"]
            return True
        else:
            return False

    if action == "latte":
        if money >= 160:
            USER["change"] = money - MENU[action]["cost"]
            resources["Money"] += MENU[action]["cost"]
            return True
        else:
            return False

    if action == "cappuccino":
        if money >= 180:
            USER["change"] = money - MENU[action]["cost"]
            resources["Money"] += MENU[action]["cost"]
            return True
        else:
            return False


def report(work):
    if work == "report":
        for ingredient in resources:
            print(f"{ingredient} : {resources[ingredient]}")


def milk_coffee(action):
    if (resources["water"] >= MENU[action]["ingredients"]["water"] and
            resources["coffee"] >= MENU[action]["ingredients"]["coffee"] and
            resources["milk"] >= MENU[action]["ingredients"]["milk"]):
        transaction_successful = transaction(action)
        if transaction_successful:
            resources["water"] -= MENU[action]["ingredients"]["water"]
            resources["coffee"] -= MENU[action]["ingredients"]["coffee"]
            resources["milk"] -= MENU[action]["ingredients"]["milk"]
            print(f"Here is your {action}. Enjoy!")
            print(f"You get Rs. {USER["change"]} returned.")
        else:
            print("Insufficient Money")
    elif resources["milk"] < MENU[action]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < MENU[action]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    elif resources["water"] < MENU[action]["ingredients"]["water"]:
        print("Sorry there is not enough water.")


def espresso(action):
    if (resources["water"] >= MENU[action]["ingredients"]["water"] and
            resources["coffee"] >= MENU[action]["ingredients"]["coffee"]):
        transaction_successful = transaction(action)
        if transaction_successful:
            resources["water"] -= MENU[action]["ingredients"]["water"]
            resources["coffee"] -= MENU[action]["ingredients"]["coffee"]
            print(f"Here is your {action}. Enjoy!")
            print(f"You get Rs. {USER["change"]} returned.")
        else:
            print("Insufficient Money")
    elif resources["coffee"] < MENU[action]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    elif resources["water"] < MENU[action]["ingredients"]["water"]:
        print("Sorry there is not enough water.")


decision = ""
while decision != "off":
    decision = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if decision == "report":
        report(decision)
    elif decision == "espresso":
        espresso(decision)
    elif decision == "latte" or decision == "cappuccino":
        milk_coffee(decision)
    else:
        print("Invalid Order")
