# # with open("weather_data.csv","r") as file:
# #     data = file.readlines()
# #     print(data)
#
#
# # import csv
# # with open("weather_data.csv", "r") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #         #print(row)
# #     print(temperatures)
#
# import pandas
# data = pandas.read_csv("weather_data.csv")
# #print(data)
# #print(data["temp"])
# #print(type(data))
#
#
# #data_dict = data.to_dict()
# # print(data_dict)
# # print(data["temp"].to_list())
# #print(sum(data["temp"].to_list()))
# #print(data["temp"].mean())
# #print(data["temp"].max())
# #print(data.condition)
#
# #print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])



import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data.head())
# print(data.columns)
print(data.groupby(["Primary Fur Color"]).count())
