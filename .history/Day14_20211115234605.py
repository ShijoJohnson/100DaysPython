from artDay14 import logo, vs
from replit import clear
from gameDataDay14 import data
import random

print(logo)
print(vs)
inGame = True
score = 0


def printscr(A, B):
  clear()
  print(logo)
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.\n")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")


def getRandInt():
  return int(random.choice(range(0, len(data)-1)))


def playGame(Anum, Bnum, score):
  printscr(data[Anum], data[Bnum])
  inp = input("Who has more followers? \nType A or B : ")
  if inp == "A" and data[Anum]['follower_count'] > data[Bnum]['follower_count']:
    return Anum
  elif inp == "B" and data[Bnum]['follower_count'] > data[Anum]['follower_count']:
    return Bnum
  else:
    print(f"Sorry, thats wrong. Final score: {score}")
    print(f"A Cont = {data[Anum]['follower_count']}, B Cont = {data[Bnum]['follower_count']}")

    return 0

Anum = getRandInt()
Bnum = 0
ret = 0
while inGame:
  Bnum = getRandInt()
  ret = playGame(Anum, Bnum, score)
  Anum = ret
  if ret == 0:
    inGame = False
  else:
    score+=1
