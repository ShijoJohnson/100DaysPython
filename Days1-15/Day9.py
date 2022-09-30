student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for i in student_scores:
  if student_scores[i] >90:
    student_grades[i] = "Outstanding"
  elif student_scores[i] >80:
    student_grades[i] = "Exceeds Expectations"
  elif student_scores[i] >70:
    student_grades[i] = "Acceptable"  
  else: 
    student_grades[i] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)








from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("\n Welcome to secret Auction\n")

loop = True
dic = {}
winner = ""
winbid = 0
while loop == True:
  name = input("What is your name?:")
  bid = int(input("What is your bid?:"))
  dic[name] = bid
  inp = input("\nAre there more bidders? yes or no\n")
  if inp == "no":
    loop = False
  clear()
  if dic[name] > winbid:
    winbid = dic[name]
    winner = name

print(f"The winner is {winner} with a bid of {winbid}")

