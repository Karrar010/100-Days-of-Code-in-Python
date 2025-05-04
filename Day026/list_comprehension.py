#list comprehension is a method used to create a list from another list,raange,tuple,string and previous we did this using a for loop, but 
# now it only needs is a single line using list comprehension
#list comprehension simplifies task and we are able to code less lines

numbers = [1,2,3,4]
new_list = [ item + 1 for item in numbers]
print(new_list)


#In python there is a concept of sequences and List,range,tuple,string follow sequence whenever we use then
name = "Yashkun"
new_name = [letter for letter in name] #the new_name was created a list type as each letter of name was split into char following a Sequence
print(new_name)

new_range = range(1,6) #from 1->5
new_range_list = [num*2 for num in new_range]
print(type(new_range))
print(new_range_list)

#CONDITIONAL LIST COMPREHENSION  Syntax: new_list  = [new_item for item in list if condition]

names = ["Alam","Bishop","Shinpachi","Aixen","Yashkun","Neo","Zulu"]
short_names_list = [name for name in names if len(name) <= 4]
all_caps_names_list = [name.upper() for name in names if len(name) > 4]
# print(short_names_list)
print(all_caps_names_list)

#challenge: get newlist with containing the square of elements
numbers_list = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [num*num for num in numbers_list] 
print(squared_numbers)

#challenge: get new list containing only the even number
even_numbers = [num for num in numbers_list if num%2 == 0]
print(even_numbers)

#challenge: print comman numbers between both files
with open("./Day26/file1.txt") as file1:
    file1_list = list(file1)
    print(file1_list)
with open("./Day26/file2.txt") as file2:
    file2_list = list(file2)
    print(file2_list)
common_number_list = [int(num) for num in file1_list if num in file2_list] #we int(num) since at that stage we add it to the new_list
print(common_number_list)
