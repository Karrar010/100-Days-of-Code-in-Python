import pandas
data =pandas.read_csv("./Day25/002 weather-data.csv")  
print(type(data)) # type function can help identity the type of file we are dealing with
#in pandas there are two data structures one is Series(1-D) and other is Dataframe(2-D), any table in a csv file can be considered as  
#Dataframe as it has both rows and columns like previous type(data)  
print(type(data["temp"])) #as for this it is a Series Data-structure it is a single column(1-D)

# print(data.info()) #through this info() we get a summary of the Dataframe

data_dict = data.to_dict()  #can convert Dataframe to other form like to a dictionary
print(data_dict)

series_to_list = data["temp"].to_list() #can convert Series datastructure to list
print(series_to_list) 

#challenge: calculate average of temperature in csv file(tip: can also use round())
print(sum(series_to_list)/len(series_to_list)) 
print(data["temp"].mean())  #can take help from the pandas Series Datastructure properties to get result Series.mean()

#challenge: get max value of temp
print(data['temp'].max())

#GET A COLUMN
print(data['day'])   #through this we print the column
print(data.day)     #pandas help convert the column name to a Dataframe attribute 

#GET A ROW
print(data[data.day == "Monday"]) #to get a certain row first select a column then select the required row
print(data[data.temp == data.temp.max()])
print(data[data.temp == data.temp.max()].condition)

#challenge: convert mondays temperature to fahrenheit
monday_temp_Fahrenheit = int(data[data.day == "Monday"].temp)*(1.8) + 32
print(monday_temp_Fahrenheit)


# CREATE A DATAFRAME FROM SCRATCH
dict_data = { 
    "order" : ["Cheese Pizza", "chicken Burger", "Shawarma Roll"],
    "amount" : [100 , 20 , 15]
}


new_dataframe = pandas.DataFrame(dict_data) #convert the dict to a dataframe 
print(new_dataframe)
new_dataframe.to_csv("./Day25/new_csv_file") #then convert dataframe to a csv file in Day25 file