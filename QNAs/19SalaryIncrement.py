"""19.Problem Description"""

"""
XYZ Technologies is in the process of increment the salary of the employees. This increment is done based on their salary and their performance appraisal rating.

 1. If the appraisal rating is between 1 and 3, the icrement is 10% of the salary
 2. If the appraisal rating is between 3.1 and 4, the increment is 20% of the Salaray
 3. If the appraisal rating is between 4.1 and 5,the increment is 30% of the salary

Sample Input 1:
  . Enter the Salary
  8000
  . Enter the Increment Score
  3
Sample output 1:
  8800  
"""

salary=int(input("Enter the salary:"))
rating=int(input("Enter the Appraisal Rating:"))
if(salary < 1 or rating < 0 or rating > 5):
  print("Invalid Input")
elif(rating > 1 and rating < 3):
  increment=(salary*10)/100
  salary=salary+increment
  print(salary)
elif(rating > 3.1 and rating < 4):
  increment=(salary*20)/100
  salary=salary+increment
  print(salary)
elif(rating>4.1 and rating<5):
  increment=(salary*30)/100
  salary=salary+increment
  print(salary)
