# myCar = ""
# def updateCar():
#     global myCar
#     myCar = "Honda"
# updateCar()
# print(myCar)

# # print("Hello")



#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
print(logo)
import random

def numberoftries(diff):
  if diff == "Easy":
    return 10
  elif diff == "Medium":
    return 7
  else:
    return 5

def gameTime():
  print("Welcome to number guessing game:")
  print("I am thinking of a number between 1 and 100")
  diff = input("Choose difficulty level: Easy, Medium or Hard: ")
  tries = numberoftries(diff)
  num = random.choice(range(1,101))

  numberGuessed = False
  while numberGuessed == False:
    inp = int(input("Enter your guess number: "))
    tries-= 1
    if inp > num:
      print("Too High")
    elif inp < num:
      print("Too Low")
    else:
      print("Guess is correct!!!")
      numberGuessed = True
    if tries == 0:
      print("No More Guesses, You lost")
      numberGuessed = True

play = True
while play == True:
  gameTime()
  contGame = input("Continue Game? y or n: ")
  if contGame == "n":
    play = False
    