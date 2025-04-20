import pandas as pd

data = pd.read_csv("./Day25/Squirrel-Census-Analysis/004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
color_column = len(data[data["Primary Fur Color"] == "Gray" ])

gray_color_count = len(data[data["Primary Fur Color"] == "Gray" ])
red_color_count = len(data[data["Primary Fur Color"] == "Cinnamon" ])
black_color_count = len(data[data["Primary Fur Color"] == "Black" ])

squirrel_dict = {
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count" : [gray_color_count,red_color_count,black_color_count]
}

new_df = pd.DataFrame(squirrel_dict)  #df == Dataframe
new_df.to_csv("./Day25/Squirrel-Census-Analysis/squirrel-count.csv")