#Oct 11th 2020
#Created by Olukemi Odujinrin

print("GPA Calculator")
print("----------------------------------------------")
print("Before we begin, we need to know what you are looking for\n")

print("Option 1: Calculate your current GPA")
print("Option 2: Calculate required average to get desired GPA\n")

option = int(input("Do you want option 1 or option 2? "))

def option1():
  course = []
  grade = []

  for i in range (5):
    c = input("Enter a course name:")
    course.append(c)
    g = input("Enter letter grade for this course:")
    grade.append(g)

  print(course)
  print(grade)

if (option == 1):
  print("Option 1\n")
  option1()
elif (option == 2):
  print("Option 2")
else:
  print("Invaild entry. Try again")