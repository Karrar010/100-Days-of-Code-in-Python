#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []  #password size is from min 12 char to max 18 char
password_letters = [random.choice(letters) for char in range(nr_letters) ] 
password_numbers = [random.choice(numbers) for char in range(nr_numbers) ] 
password_symbols = [random.choice(symbols) for char in range(nr_symbols) ]
password_list.append(password_letters,password_numbers,password_symbols)

random.shuffle(password_list)

password = "".join(password_list) #this a shortcut to joins string will either list elements or tuple or even dict elements
# if mylist = ["1","2","3"] then pass = "#".join(mylist) ---->>>gives>>> pass-->>>"1#2#3"

print(f"Your password is: {password}")