#higher lower game 
from art import logo #import the ascii art from other file 
from art import vs
from game_data import data
import random
import os

print(logo)
playerA = {}
playerB = {}

playerA = random.choice(data) #will get random individual for each A and B
playerB = random.choice(data) 
score = 0

def switcher(playerA, playerB): 
    """switches the players being compared after each action by user"""
    playerA = playerB
    playerB= random.choice(data)
    return (playerA, playerB) #return two dicts

while True:
    if playerA['follower_count'] > playerB['follower_count']: #help find player will higher followers
        morefollowers = 'A'
    elif playerA['follower_count'] < playerB['follower_count']:
        morefollowers = 'B'
    else:
        morefollowers = 'X'

    print(f"Compare A: {playerA['name']} , {playerA['description']} , from {playerA['country']} \n") 
    print(vs)
    print(f"Against B: {playerB['name']} , {playerB['description']} , from {playerB['country']} \n")
    decision = input("Who has more followers on instagram? 'A' or 'B' : ") #user gives input

    if decision == morefollowers:  #checks if decision is right or wrong
        score = score +1
        os.system('cls')
        print(f"Your Right!!!. Current Score : {score}")
        playerA,playerB = switcher(playerA,playerB)  #assign each dict being return to the right player dictionary

    elif morefollowers == 'X': #special condtion when both the players being compared are same
        score = score +1
        os.system('cls')
        print(f"Both Have same number of followers.. Point Given.. Current Score : {score}")
        playerA,playerB = switcher(playerA,playerB)
    else:
        os.system('cls') #clears the terminal screen at run times
        print(f"\nSorry!! That's Wrong, Final Score : {score}")
        break 


