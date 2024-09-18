#password generator
import random

print("\tPASSWORD GENERATOR")
cho1 = int(input("What should be number of letter in Password? "))
cho2 = int(input("How many number should be in the Password? "))
cho3 = int(input("What should be number of special characters in Password? "))

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ["1","2","3","4","5","6",'7','8','9']
special = ["!","@","#","$","%","&","(",")","?"]

#easymethod
# password = ""
# for x in range(1,cho1+1):
#     password= password + random.choice(alphabets) #concatenating 4 letters
# for y in range(1,cho2+1):
#     password = password + random.choice(number)
# for z in range(1,cho3+1):
#     password = password + random.choice(special)
# print("password",password)       #result : aybs29@#  kinda in order of letter->nums->special char


#hardmethod :    password contain letter, numbers, special char in random order
password = ""
num1=0
num2=0
num3=0
for x in range(1,(cho1+cho2+cho3)*2): #bc sometime in loop rand func might select number or other even after adding them to password to avoid this we increase the size of loop
    decision = random.randint(1,3)
    if decision == 1:
        num1+=1
        if num1<=cho1:
            password= password + random.choice(alphabets)
    elif decision == 2:
        num2+=1
        if num2<=cho2:
            password = password + random.choice(number)
    else:
        num3+=1
        if num3<=cho3:
            password = password + random.choice(special)

print("password",password)

#or in another hard method you could create a password list instead of string here
# and add all values into it and then create a password from by using ramdom func
# meaning: password =[a,b,e,k,5,9,@,$]
#then we use rand like final_password = final_password + rand.choice(password) in a for loop of size=len(password)