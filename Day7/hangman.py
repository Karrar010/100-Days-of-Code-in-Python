#hangmangame
import random
def loser(lose,times_wrongg):
    if lose == 0:
        if times_wrongg == 1:
            print(" _______\n"
                "|/      |\n"
                "|      \n"
                "|       \n"
                "|       \n"
                "|       \n"
                "|\n"
                "|_\n")
        elif times_wrongg ==2:
            print(" _______\n"
                "|/      |\n"
                "|      (_)\n"
                "|       \n"
                "|       \n"
                "|       \n"
                "|\n"
                "|_\n")
        elif times_wrongg ==3:
            print(" _______\n"
                "|/      |\n"
                "|      (_)\n"
                "|       |\n"
                "|       |\n"
                "|       \n"
                "|\n"
                "|_\n")
        elif times_wrongg ==4:
            print(" _______\n"
                "|/      |\n"
                "|      (_)\n"
                "|      \|/ \n"
                "|       |\n"
                "|       \n"
                "|\n"
                "|_\n")
        elif times_wrongg ==5:
            print(" _______\n"
                "|/      |\n"
                "|      (_)\n"
                "|      \|/ \n"
                "|       |\n"
                "|      / \ \n"
                "|\n"
                "|_\n")
print(" _\n| |\n| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  \n"
"| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n"
"| | | | (_| | | | | (_| | | | | | | (_| | | | |\n"
"|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n"
"                   __/  |                      \n"
"                   |____/       \n")
print(" _______\n"
     "|/      \n"
     "|      \n"
     "|      \n"
     "|       \n"
     "|      \n"
     "|\n"
    "|_\n")

word_list = ["icecream","insect","jet","fighter","kaleidoscope","leather","jacket","leg","library","liquid","magnet","manga","mappa"]
word_rand = random.choice(word_list)

guess_word = []
time_right = 0
times_wrong = 0
for x in range(1,len(word_rand)+1):
    guess_word += "_"
while True:
    print(guess_word)
    loserpath = -1
    inp = input("Guess Word(one letter at a time): " ).lower()
    if inp in guess_word:
        print(f"You have already guessed {inp}, so you lost a live")
        times_wrong+=1
        loserpath = 0
        loser(loserpath,times_wrong)
        for y in range(0,len(guess_word)):
            if guess_word[y]== inp:
                time_right-=1
                    
    for x in range(0,len(word_rand)):
        if inp == word_rand[x]:
            guess_word[x]= inp
            loserpath = -1
            time_right+=1
    
    if inp not in word_rand:
        times_wrong +=1
        loserpath=0
        loser(loserpath,times_wrong)
    if time_right==len(word_rand):
        print(guess_word)
        print("Result: YOU WIN!!!  GUY LIVED HAPPILY EVER AFTER")
        break
    if times_wrong == 5:
        print(guess_word)
        print(word_rand)
        print("Result: YOU LOSE!!! GUY DIED A PAINFUL DEATH")
        break