# uses csv files to read data and organizes them into a dictionary and vice versa
with open("weather_data.csv") as weather_data:
    weather_list = weather_data.readlines()
    print(weather_list)

import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

... import pandas
... 
... data = pandas.read_csv("weather_data.csv")
... # print(type(data["temp"]))
... # series: single column in list
... # dataframe: whole table
... 
... # print(data["condition"])
... # print(data.condition)
... 
... # get data in row (can use conditions)
... # print(data[data.day == "Monday"])
... # print(data[data.temp == data.temp.max()])
... 
... # monday = data[data.day == "Monday"]
... # print(monday.temp * (9/5) + 32)
... 
... # create a dataframe from scratch
... data_dict = {
...     "students": ["Amy", "James", "Angela"],
...     "scores": [76, 56, 65]
... }
... data = pandas.DataFrame(data_dict)
... data.to_csv("new_data.csv")
... 
... # gray, cinnamon, and black
... import pandas as pd
... 
... data = pd.read_csv("squirrel_data.csv")
... gray = len(data[data["Primary Fur Color"] == "Gray"])
... cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
... black = len(data[data["Primary Fur Color"] == "Black"])
... 
... color_dict = {
...     "fur color": ["gray", "cinnamon", "black"],
...     "count": [gray, cinnamon, black]
... }
... df = pd.DataFrame(color_dict)
... df.to_csv("squirrel_count.csv")
