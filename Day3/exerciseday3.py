#find if a given year is a leap year or not

# print("Leap Year Detector")

# while(True):
#     year = int(input("Enter a Year to Check:  "))
#     if year % 4 == 0 and year % 100 == 0 or year%400==0:
#         print(f"Result: {year} is a leap year")
#     else:
#         print(f"Result: {year} is not a leap year")


#pizza plaza order your pizza
print("Welcome to Pizza Plaza")
type_piz = input("what type of  pizza do you want?\nSmall(S), Medium(M) ,Large(L)   Chose: ")
addpep = input("Do you want to add Peparoni? Y or N  Ans: ")
addchez = input("Do you want to add Extra Cheese? Y or N  Ans: ")
if type_piz == "S": 
    bill= 15
    if addpep == "Y": 
        bill += 2
elif type_piz == "M":
    bill= 20
    if addpep == "Y": 
        bill += 3
else:
    bill= 25
    if addpep == "Y": 
        bill += 3
if addchez =="Y":
            bill += 1
print(f"Sir your Total Bill is {bill}")



#Love Calculator
print("\tLove Calculator")
you = input("Enter Your Name: ")
their = input("Enter their Name: ")
name1 = you.lower()
name2 = their.lower()
combine_name = name1+name2
t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")
l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
# e = name1.count("e")

# print(f"t= {t},r = {r},u = {u},e={e},  l ={l},o={o},v={v},e={e} ")
dig1 = t+r+u+e
dig2 = l+o+v+e
total = dig1*10+dig2
if total <= 10 or total>= 90:
    print(f"Your Love Score is {total}%, you both go like coke and mentos")
elif total >=40 and total <=50:
    print(f"Your Love Score is {total}%, you both look great together")
else:
    print(f"Your Love Score is {total}%, look for another person")





