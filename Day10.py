# def titleName(fname, lname):
#     name = fname.title() +" "+ lname.title()
#     return name
# print(titleName("sdsfds", "HKJHKHK"))


def is_leap(year):
  """Checks if a leap year"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and (month == 2):
    return 29
  else:
    return month_days[month-1]
  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)














def add(i,j):
  return i+j

def substract(i,j):
  return i-j  

def multiply(i,j):
  return i*j  

def divide(i,j):
  return i/j 

operations = {"+": add, "-": substract, "*": multiply, "/": divide}


i = int(input("Enter number 1:"))
j = int(input("Enter number 2:"))
ops = input("Enter operaion:")
funce = operations[ops]
results = funce(i,j)
print (f"Result is {results}")




def add(i,j):
  return i+j

def substract(i,j):
  return i-j  

def multiply(i,j):
  return i*j  

def divide(i,j):
  return i/j 

operations = {"+": add, "-": substract, "*": multiply, "/": divide}
i = int(input("Enter number 1:"))
  
cont = True
while cont:
  j = int(input("Enter next number:"))
  ops = input("Enter operaion:")
  funce = operations[ops]
  results = funce(i,j)
  i = results
  print (f"Result is {results}")
  if input("Continue? y or n") != "y":
    cont = False




#Start Anew
def add(i,j):
  return i+j

def substract(i,j):
  return i-j  

def multiply(i,j):
  return i*j  

def divide(i,j):
  return i/j 

operations = {"+": add, "-": substract, "*": multiply, "/": divide}
def calculator():
  i = int(input("Enter number 1:"))
  
  cont = True
  while cont:
    j = int(input("Enter next number:"))
    ops = input("Enter operaion:")
    funce = operations[ops]
    results = funce(i,j)
    i = results
    print (f"Result is {results}")
    if input("Continue? y or n to start anew") != "y":
      #cont = False
      calculator()

calculator()
