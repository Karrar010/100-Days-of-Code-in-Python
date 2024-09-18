# list = ["a","b","c","d"]

# for x in list:  #here x is used to indicate the values in list like i in c++
#     print(x)    #the loop runs depending on the size of list which here is 4

# Task 1   :   Average of height
sum = 0
height  = [188,190.3,167.3,200,187,164.7]
print("Heights: ",height)
for x in height:
    sum = sum+ x
print("Average Height is ",round(sum/len(height)))

#Task 2 : finding the highest height
print(max(height))
maximus = 0
for x in height:
    if maximus < x:
        maximus = x 
print("Highest Value : ", maximus)


#Task 4: Summation of numbers in range(1,101)
sum =0
for x in range(1,101):
    sum += x
print(sum)

#task 5: Adding even numbers
sum_even =0
for x in range(0,101,2):
    # print(x)
    sum_even += x
print(sum_even)