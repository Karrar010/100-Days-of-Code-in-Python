#FINDING THE CANS OF PAINT FOR A GIVEN AREA OF WALL

#TIP: 1 can of paint covers 5 square meters of wall
import math
def cans(width,height):
    coverage =5
    area = width*height
    number_of_cans = area/coverage
    print(f"Number of cans required for wall = {math.ceil(number_of_cans)}") #i could not used round because if e.g 3.2 round(3.2) = 3
print("|| CAN CALCULATER ||\n")
height_input = int(input("Heigth of wall= "))
Width_input = int(input("Width of wall= "))
cans(height_input,Width_input)


#PRIME NUMBER CHECKER
def prime(number):
    check=0
    for x in range(2,number+1):
        if number%x == 0:
            check+=1
    if check==1:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is NOT a prime number")
        

number1 = int(input("Integer: "))
prime(number1)