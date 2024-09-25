print(""" _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\_
                    _/ |                
                    |__/   
Rules:
    Try to get as close to 21 without going over.
    Kings, Queens,Jacks and card numbered 10 are worth 10 points.
    Aces are worth 1 point.
    Cards 2 through 9 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    In case of a tie, or score over 21 game over.
    The Dealer must not Hit after 17 score.\n""")
    
import random as rand
#getting card function
total_cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]
def getcard():
    return rand.choice(total_cards)
#showing result function
def resultofgame(p1point,computer_point):
    sum_p1 = sum(p1point)
    sum_comp = sum(computer_point)
    if sum_p1 > 21:
        print("Your Final Hand: ", p1point)
        print("Computer's Final Hand: ", computer_point)
        print("YOU LOSE, YOU WENT OVER 21 !!!!")
    elif sum_comp > 21:
        print("Your Final Hand: ", p1point)
        print("Computer's Final Hand: ", computer_point)
        print("YOU WIN, COMPUTER WENT OVER 21 !!!!")
    elif sum_p1 > sum_comp:
        print("Your Final Hand: ", p1point)
        print("Computer's Final Hand: ", computer_point)
        print("YOU WIN!!!!")
    elif sum_p1 < sum_comp:
        print("Your Final Hand: ", p1point)
        print("Computer's Final Hand: ", computer_point)
        print("YOU LOSE!!!!")
    else:
        print("Your Final Hand: ", p1point)
        print("Computer's Final Hand: ", computer_point)
        print("GAME DRAW!!!!")
        

p1point = [getcard(),getcard()]
computer_point = [getcard(),getcard()]


print("Your cards : ",p1point)
print(f"Computer's first card: {computer_point[0]}")

#values of player and computer cards
sum_p1 = sum(p1point)
sum_comp = sum(computer_point)

while True:
    if sum_comp < 22 and sum_p1  < 22:    
        hit = input("Type \"y\" to get another card, otherwise press anything: ")
        if hit == "y":
                print("\n-----<>>>> Player Hit a Card <<<<>-----")
                p1point.append(getcard())
                print("Your cards : ",p1point)
                print(f"Computer's cards: {computer_point[0]}")
                sum_p1 = sum(p1point)
        else:
            resultofgame(p1point,computer_point)
            break
        if sum_comp < 17:
                print("\n-----<>>>> Computer Hit a Card <<<<>-----")
                computer_point.append(getcard())  
                print("Your cards : ",p1point)
                print(f"Computer's cards: {computer_point[0]}\n") 
                sum_comp = sum(computer_point)
    else: 
        resultofgame(p1point,computer_point)
        break
