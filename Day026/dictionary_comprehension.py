#similar to list comprehension through dictionary comprehension we simplify our code and
# create dictionary from a list,tuple,string,dictionary,range
#SYNTAX:
# new_dict = { newkey: newvalue for item in list} #also with if statements
# new_dict = { newkey: newvalue for (key,value) in dict.item()} #also with if statements

names = ["Alam","Bishop","Shinpachi","Aixen","Yashkun","Neo","Zulu"]
import random
student_score_dict = { student: random.randint(1,100)  for student in names}
print(student_score_dict)

passed_Students_dict = { student: Score  for (student,Score) in student_score_dict.items() if Score > 40}
print(passed_Students_dict)

#challenge: create a dict that calculates the number of letters for each word in sentene
sentence = "what is the Airspeed Velocity of an Unladen Swallow?"
words_dict = {word: len(word) for word in sentence.split(' ')}
print(words_dict)

#challenge: create a new dict init convert the temp to fahrenheit
weather_c = {
    'Monday':12, 
    'Tuesday':14, 
    'Wednesday':15, 
    'Thursday':14, 
    'Friday':21,   
    'Saturday':22,
    'Sunday':24
}

weather_in_F = {day: (temp*1.8)+32 for (day,temp) in weather_c.items()} #usage of items() is that it groups key:values together inside a list
print(weather_in_F)

# ITERATIONS THROUGH A DATAFRAME

# loop through a dictionary: previously we have done this
# for (key,value) in dict.item():
    # print(key)

import pandas

students_record = {
    "student" : ["Zeus","Noir","Plank","Khan"],
    "marks": [39,93,40,88]
}
student_dataframe = pandas.DataFrame(students_record)
print(student_dataframe)
# loop through a  dataframe
# for (key,value) in student_dataframe.items():
#     print(value)

#so pandas has inbuilt attribute for looping through rows of dataframe
for (index,row) in student_dataframe.iterrows(): #select a index and row  acc to it 
    print(row)
    # print(row.student)