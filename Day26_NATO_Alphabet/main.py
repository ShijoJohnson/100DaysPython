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


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(temp*9/5)+32 for (day,temp) in weather_c.items()}
print(weather_f)


