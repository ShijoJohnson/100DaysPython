# print("hello"[0])
# print("hello"[-1])

# print(123)
# print(123_456_789)

# print(type(123))


# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆
# ####################################
# #Write your code below this line 👇
# str1 = str(two_digit_number)
# print(int(str1[0]) + int(str1[1]))

# print(3*3+3/3-3)

# print(int(8/3))

# print(round(8/3))

# score = 100
# height = 1.8
# name = "Shijo"
# male = True
# print(f"Hi {name}, your score is {score}. your height is {height}, you are a male? {male}")

# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆

#Write your code below this line 👇

# intAge = int(age)
# days = (90-intAge)*365
# weeks = (90-intAge)*52
# months = (90-intAge)*12
# print(f"You have {days} days, {weeks} weeks, {months} months left.")


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪




# Instructions
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Example Input
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
#Each person should pay: $19.93
#Write your code below this line 👇
# print("Welcome to the tip calculator!")
# amt = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# pplCount = int(input("How many people to split the bill? "))

# perPay = (amt/pplCount)
# perPayNTip = round((perPay + perPay*tip/100),2)
# print(f"Each person should pay: {perPayNTip}")


print(round(2.3,3))
print("{:.3f}".format(2.3))