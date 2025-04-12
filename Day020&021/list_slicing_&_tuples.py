name = "Galahad"
list = list(name) #converted string to list
name_tuple = ("l","a","n","c","y")

print(list)

# list slicing
print(list[2:5]) # first : colon help specify the range
print(list[::-1]) # second colon is used jumping
print(list[1:5])
print(list[1:5:2])
print(list[1:5:3])

#tuple slicing
print(name_tuple[1:4:1])
print(name_tuple[1:])
print(name_tuple[1::])
