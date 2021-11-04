# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
cnt = 0
tot_Height = 0
for student in student_heights:
  cnt+=1
  tot_Height = tot_Height+student

print(round(tot_Height/cnt))





# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_score = 0
for score in student_scores:
  if score>max_score:
    max_score = score

print(f"The highest score in the class is: {max_score}")


