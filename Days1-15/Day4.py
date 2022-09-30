# #Write your code below this line 👇
# #Hint: Remember to import the random module first. 🎲

# import random
# num = random.randint(0,1)
# if num == 0:
#   print("Heads")
# else:
#   print("Tails")



# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# import random
# numPpl = len(names)
# randNum = random.randint(0,numPpl-1)
# print(f"{names[randNum]} is going to buy the meal today!")





# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# map_col=int(position[0])-1
# map_row=int(position[1])-1

# map[map_row][map_col]="X"



# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")






rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
userInp = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
compInp = random.randint(0,2)
outputAscii = [rock, paper,scissors] 
print(f"Your choice is \n {outputAscii[userInp]}")
print(f"Computer choice is \n {outputAscii[compInp]}")

if userInp == compInp:
  print("Draw")
elif (userInp == 0 and compInp == 1) or (userInp == 1 and compInp == 2) or (userInp == 2 and compInp == 0):
  print("You lose")
else:
  print("You Win")
