import csv   #inbuilt library for csv file reading and writing
#but for complex csv files we use pandas library


# with open(file="./Day25/002 weather-data.csv") as file:
#     data = csv.reader(file)
#     temperature = [] #challenge: get all the tempertures of week in int form into this temp list
#     for row in data:
#         if row[1] != 'temp':#if statement to avoid the row[1] == 'temp'
#             temperature.append(int(row[1]))
#         # print(row) #this prints each row of the csv file as the loop iterates
#     print(temperature)
        

import pandas as pd

data =pd.read_csv("./Day25/002 weather-data.csv")  #as compared to csv library we need only a single line to do lengthy task in pandas
print(data)     
print(data["temp"])  #completed previous challenge in a single line