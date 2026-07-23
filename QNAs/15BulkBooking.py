"""15.Problem Description"""

"""
In a theater, there is a discount scheme announced where one gets a 10% discount on the total cost of tickets when there is bulk booking of more than 20 tickets, and a discount of 2% on the total cost of tickets if a special coupon card is submitted. Develop a program to find the as per the scheme.The cost as per the scheme. The cost of the k class ticket is Rs75 and q class Rs 150.
Refreshment can also be opted by paying an additional of Rs 50 per member.

Hint: K and q you have to book minimum of 5 tickets and maximum of 40 at a time. If fails display "Minimum of 5 and maximum of 40 at a time.If fails displays "minimum of 5 and maximum of 40 Tickets". If circle is given a value othar than "k" or "q"  the output should be "invalid input"

The ticket cost should be printed exactly to two decimal places.


Sample Input 1:
  -Enter  the no of ticket:35
  -Do you want refreshment:y
  -Do you have coupon code:y
  -Enter the circle:k

Sample output 1:
  -Ticket cost:4065.25  
"""

import sys
noTicket=int(input("Enter the no of ticket: "))

if(noTicket<5 or noTicket>40):
  print("Minimum of 5 and Maximum of 40 ticket")
  sys.exit(0)

ref=input("Do you want refreshment: ")

co=input("Do you have any coupon code:")

circle=input("Enter the circle:")

if(circle=="k"):
  cost=75*noTicket
elif(circle =='q'):
  cost=150*noTicket
else:
  print("invalid Input")
  sys.exit(0)
total=cost
if(co=='y'):
  total=cost-((0.02)*cost)

if(ref=='y'):
  total+=(noTicket*50)

print("Tickets cost:{}".format(round(total,2)))  