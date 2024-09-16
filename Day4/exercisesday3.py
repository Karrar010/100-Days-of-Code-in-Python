#head or tails
import random
result_int = random.randint(0,1)
print("\tCoin Toss")
input("Press Enter to Start.. ")
if result_int == 0:
    print("Result:  Head")
else:
    print("Result:  Tail") 


#restaurant bill payer selector
import random

strin = "alan , karim , faryaan , lucas"
list = strin.split(" , ")
print(list)
rando = random.randint(0,len(list)-1)
print(f"{list[rando]} will be paying the resturant bill")


#   EXTRAAA
stri = " hi , my name , is , alan , walker "
list =  stri.split(" , ")

print(list)


#treasure map
rowlist1 = [" O "," O "," O "]
rowlist2 = [" O "," O "," O "]
rowlist3 = [" O "," O "," O "]
map = [rowlist1,rowlist2,rowlist3]
print(f"{rowlist1}\n{rowlist2}\n{rowlist3}")
choice = input("Enter the Place where you want to put the treasure: Ans: " )  #enter two number col num, row num

map[int(choice[0])-1][int(choice[1])-1] = " X "

print(f"{rowlist1}\n{rowlist2}\n{rowlist3}")