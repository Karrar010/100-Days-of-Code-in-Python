# Coffee Machine
#-------------------------------------
#TIP : ADD MORE FUNCTIONS TO THE PROGRAM BY REMOVING CONDITIONAL STATEMENTS
#-------------------------------------
from main_coffee import resource
from main_coffee import menu
from main_coffee import logo

money = 0
print(logo)
def cashier():
    print("please insert coins: ")
    quarters = int(input("1. Quaters: "))
    dime = int(input("2. Dimes: "))
    nickle = int(input("3. Nickles: "))
    penny = int(input("4. Pennies: "))
    amount_entered = (0.25*quarters) + (0.1*dime) + (0.05*nickle) + (0.01*penny)
    return amount_entered

e_water = menu["espresso"]["ingredients"]["Water"]
e_coffee = menu["espresso"]["ingredients"]["Coffee"]
l_water = menu["latte"]["ingredients"]["Water"]
l_milk = menu["latte"]["ingredients"]["Milk"]
l_coffee = menu["latte"]["ingredients"]["Coffee"]
c_water = menu["cappuccino"]["ingredients"]["Water"]
c_milk = menu["cappuccino"]["ingredients"]["Milk"]
c_coffee = menu["cappuccino"]["ingredients"]["Coffee"]

while True:
    choice = input("What would you like? (espresso/latte/cappuccino) or (report): ")
    if choice.lower() == "espresso":
        if e_coffee > resource["Coffee"]:
            print("Sorry their is not enought milk")
        elif e_water > resource["Water"]:
            print("Sorry their is not enough water")
        else:
            amount = cashier()
            change = amount - 1.5
            money = money + 1.5
            if change < 0:
                print("Sorry their isn't enough money. Money refunded")
                change = amount + 1.5
                money = money - 1.5
                break
            resource["Water"] = resource["Water"] - e_water
            resource["Coffee"] = resource["Coffee"] - e_coffee
            print(f"Here is you change: ${round(change,2)}\nHere is your espresso!!")
    elif choice.lower() == "latte":
        if l_coffee > resource["Coffee"]:
            print("Sorry their is not enough milk")
        elif l_water > resource["Water"]:
            print("Sorry their is not enough water")
        elif l_milk > resource["Milk"]:
            print("Sorry their is not enough Milk")
        else:
            amount = cashier()
            change = amount - 2.5
            money = money + 2.5
            if change < 0:
                print("Sorry their isn't enough money. Money refunded")
                change = amount + 2.5
                money = money - 2.5 
                break
            resource["Water"] = resource["Water"] - l_water
            resource["Milk"] = resource["Milk"] - l_milk
            resource["Coffee"] = resource["Coffee"] - l_coffee
            print(f"Here is you change: ${round(change,2)}\nHere is your latte!!")
    elif choice.lower() == "cappuccino":
        if c_coffee > resource["Coffee"]:
            print("Sorry their is not enough milk")
        elif c_water > resource["Water"]:
            print("Sorry their is not enough water")
        elif c_milk > resource["Milk"]:
            print("Sorry their is not enough Milk")
        else:
            amount = cashier()
            change = amount - 3.0
            money = money + 3.0
            if change < 0:
                print("Sorry their isn't enough money. Money refunded")
                change = amount + 3.0
                money = money - 3.0 
                break
            resource["Water"] = resource["Water"] - c_water
            resource["Milk"] = resource["Milk"] - c_milk
            resource["Coffee"] = resource["Coffee"] - c_coffee
            print(f"Here is you change: ${round(change,2)}\nHere is your cappuccino!!")  
    elif choice.lower() == "report":
        print(resource)
        print(f"Money: ${money}")
    else:
        break