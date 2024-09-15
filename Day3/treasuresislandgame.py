print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Treasure]
*******************************************************************************''')
print("Welcome to Treasure Hunter")
choice0 = int(input("1. Play the Game       2. Exit(enter any input)     Ans: "))
if choice0==1:
    choice = input("Where do you want to go? Left or Right : ")
    if choice == "left" or choice == "Left":
        print("On left side, You see a hill and move towards it.")
        choice2 = input("Do you want to walk towards the hill or use a Vehicle? Ans: ")
        if choice2 == "walk" or choice2 == "Walk":
            print("You Reach the Hill top and find a hut.")
            choice3 = input("Do you want to open the hut? Yes or No : ")
            if choice3=="Yes" or choice3 =="yes":
                print("You Open the Hut and there is nothing in it.")
                print("You Lose... Game Over:(")
            else:
                print("You donot find the treasure")
                print("You Lose.. Game Over :(")
        else:
            print("You use the Vehicle but the half way through No Fuel is left")
            print("You Lose.... Game Over :(")
    elif choice == "Right" or choice== "right":
        print("On right side, You see the Jungle and in the jungle there is a Cave")
        choice4 = input("Do you want to go towards the cave or you want to Camp outside? Cave or Camp Ans: ")
        if choice4=="Cave" or "cave":
            print("You go into the cave and find a Chest.")
            choice5= input("Do you wanna Open the Chest? Yes or No Ans: ")
            if choice5 == "Yes" or "yes":
                print("Congratulations..... YOU WON THE GAME :)")
            else:
                print("You lost once in a life time Opportunity... Game Over :(")
        else:
            print("Camping Seriously... you chould have become Rich but you choose to Camp")
            print("For such a lame and unimportant decision, You Lose... Game Over :(")
    else:
        print("Invalid Input... Restart Game")

else:
    print("Exited...")