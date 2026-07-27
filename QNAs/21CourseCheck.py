"""21.Problem Description"""

"""
IIHM institution is offering a variety of courses to students.Students have a facility to check whether a patricular course is available in the instituion. Write a program to help the institution accomplish this task.
If the number is less than or equal to zero display "Invalid Range".

Assume maximum number of courses is 20.

Sample Input 1:
  . Enter no course: 5
  . Enter course names: 
    Java
    Oracle
    C++
    MySQL
    Dotnet
  . Enter the course to be searched
    C++

Sample Output 1
  C++ course is available

"""

n=int(input("Enter no of course:"))
if not(n>0 or n<20):
  print("Invalid Range")
  exit()

course=[]
print("Enter the courses names:")
for i in range(n):
  course.append(input())

search=input("Enter the courses to be searched:")

if search in course:
  print(search,"Course is available")
else:
  print(search,"Course is not available")