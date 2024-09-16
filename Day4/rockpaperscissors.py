import random

print("\tRock Paper Scissor")
while True:
    choice_2 = int(input("Choice ONE of the following:\n 1. Rock\t 2. Paper \t 3. Scissors  \nANSWER: "))
    print(f"You choose {choice_2}")
    result_int = random.randint(1,3)
    if choice_2!=result_int:
        if choice_2 == 1 and result_int == 2:
            print("Computer : Scissors\nYou: Rock\t YOU WIN!!")
        elif choice_2 == 1 and result_int == 3:
            print("Computer : Paper\nYou: Rock\t YOU LOSE!!")
        elif choice_2 == 2 and result_int == 1:
            print("Computer : Rock\nYou: Paper\t YOU WIN!!")
        elif choice_2 == 2 and result_int == 3:
            print("Computer : Scissors\nYou: Paper\t YOU LOSE!!")
        elif choice_2 == 3 and result_int == 1:
            print("Computer : Rock\nYou: Scissors\t YOU LOSE!!")
        elif choice_2 == 3 and result_int == 2:
            print("Computer : Paper\nYou: Scissors\t YOU WIN!!")

        break
    else:
        print("Its a DRAW!!  Restart Game")


