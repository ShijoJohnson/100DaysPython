# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if (number%2) == 0:
#   print("This is an even number.")
# else (number%2) == 1:
#   print("This is an odd number.")




# height = int(input("Enter your height:"))

# if height > 120:
#     age = int(input("Enter your age:"))
#     if age > 18:
#         print("ticket is $12")
#     elif age > 10:
#         print("ticket is $10")
#     else:
#         print("ticket is $7")
# else:
#     print("Sorry, you cannot ride!")
    


# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = round(weight/(height ** 2),2)
# if bmi < 18.5:
#   print(f"Your bmi is {bmi}. You are weight")
# elif bmi < 25:
#   print(f"Your bmi is {bmi}. You are normal weight")
# elif bmi < 30:
#   print(f"Your bmi is {bmi}. You are slightly overweight")
# elif bmi < 35:
#   print(f"Your bmi is {bmi}. You are obese")
# else:
#   print(f"Your bmi is {bmi}. You are clinically obese")



# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if year%4 != 0:
#   print("Not a Leap year")
# elif(year%100 != 0):
#   print("Leap Year")
# elif(year % 400 ==0):
#   print("Leap year")
# else:
#   print("Not Leap year")



# height = int(input("Enter your height:"))
# bill = 0
# if height > 120:
#     age = int(input("Enter your age:"))
#     if age > 18:
#         bill = 12
#         print("ticket is $12")
#     elif age > 10:
#         bill = 10
#         print("ticket is $10")
#     else:
#         bill = 7
#         print("ticket is $7")
#     photo = input("Do you want a photo? Y or N:")
#     if photo == 'Y':
#         bill += 20
#     print(f"Total bill is {bill}")
# else:
#     print("Sorry, you cannot ride!")


# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bill = 0
# if size == "S":
#   bill+=15
# elif size == "M":
#   bill+=20
# else:
#   bill+=25
# if add_pepperoni == "Y" and size =="S":
#   bill+=2
# elif add_pepperoni == "Y" and size !="S":
#   bill+=3
# if extra_cheese == "Y":
#   bill+=1

# print(f"Your final bill is: ${bill}.")  






# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# name1_low = name1.lower()+name2.lower()
# true_Cnt = name1_low.count("t") + name1_low.count("r") + name1_low.count("u") + name1_low.count("e")
# love_Cnt = name1_low.count("l") + name1_low.count("o") + name1_low.count("v") + name1_low.count("e")

# score = int(str(true_Cnt) + str(love_Cnt))

# if score <10 and score > 90:
#   print(f"Your score is {score}, you go together like coke and mentos")
# elif score > 40 and score < 50:
#   print(f"Your score is {score}, you are alright together")
# else:
#   print(f"Your score is {score}.")



print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_Resp = input("which way? left or right?")
if first_Resp == "left":
  second_Resp = input("Reached lake.. Wait or Swim??")
  if second_Resp == "Wait":
    third_Resp= input("Boats came, yacht or boat?")
    if third_Resp == "boat":
      print("Treasure is your, you WIN!!!")
    else:
      print("Bezo ate you for Dinner:(")
  else:
    print("You swam and shark ate you")
else:
  print("You fell off cliff, game over")