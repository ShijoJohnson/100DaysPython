# # lst = [i*2 for i in range(1,5)]
# # print(lst)
# #
# # lst1 = [i*2 for i in range(1,5) if i%2 ==0]
# # print(lst1)
# #
# import random
#
# names = ['Alex', 'Beth', 'Caroline', 'Raj', 'Jack', 'Susan']
# student_scores = {item: random.randint(20, 100) for item in names}
# print(student_scores)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day:(temp*9/5)+32 for (day,temp) in weather_c.items()}
# print(weather_f)


# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# DoneTODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
#print(df.head(5))
dict1 = {row.letter:row.code for (index, row) in df.iterrows()}
print(dict1)


# DoneTODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = list(input("Enter your name: ").upper())
# print(name)
result = [dict1[char] for char in name]
print(result)


