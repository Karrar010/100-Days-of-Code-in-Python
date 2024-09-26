print(""" /$$   /$$                         /$$                            /$$$$$$                                                            
| $$$ | $$                        | $$                           /$$__  $$                                                           
| $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ | $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/ /$$__  $$ /$$__  $$
| $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$ | $$$$$$$$| $$  \__/
| $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      | $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$| $$_____/| $$      
| $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      |  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/|  $$$$$$$| $$      
|__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/       \______/  \______/  \_______/|_______/|_______/  \_______/|__/      
                                                                                                                                     
                                                                                                                                     
                                                                                                                                     """)
import random
print("\nNumber is between 1 and 100")
rand_num = random.randint(1,100)

def guess_guider(chance):
    for x in range(chance):
        guess_num = int(input("Guess Number: "))
        if rand_num > guess_num:
            print("Too Low...")
            print(f"You have {chance - x - 1} attempts left.")
        elif rand_num < guess_num:
            print("Too High...")
            print(f"You have {chance - x - 1} attempts left.")
        else:
            print("Congratulations! You guessed the correct number!")
            return True
    return False
    
diffi = input("Choose level of difficulty:  easy(e) or hard(h) Ans: ")
if diffi.lower() == "e":
    chance = 10
    game_result = guess_guider(chance)
    if game_result:
        print("You Won!!!")
    else: 
        print(f"You Lost!!! Number Was {rand_num}")
elif diffi.lower() == "h":
    chance = 5
    game_result = guess_guider(chance)
    if game_result:
        print("You Won!!!")
    else: 
        print(f"You Lost!!! Number Was {rand_num}")
else:
    print("Invalid Input!!!! RESTART GAME...")
