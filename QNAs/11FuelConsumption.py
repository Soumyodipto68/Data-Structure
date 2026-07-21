"""11 Problem Description"""

"""
Write a program to calculate the fuel consumption of your truck.The program should ask the user to enter the quantity of diesel to fill up the bank and the distance covered till the tank goes dry.Calculate the fuel consumption and display it in the format (liters per 100 kilometers).

convert the same result to the US style of miles per gallon and display the result. If the qualites or distance is zero or negetive display "is an invalid Input".

[Note: The US approach of fuel consumption calculate (distance/fuel) is the invense of the European approach (fuel/distance).Also note that 1 kilometer is 0.6214 miles, and 1 liter is 0.2642 gallons.]

The result should be with decimal place.To get decimal place.To get two decimal place refer the below-mentioned print statement:

float cost = 670.23;
print(f"You need a sum of Rs.%2f to cover the trip",cost)

Sample Input 1:
- Enter the no of liters to fill the tank 20
- Enter the distance covered 150

Sample Output 1:
- Liters/100KM 13.33
- Miles/gallons 17.64
"""

import sys

print("Enter the no liters to fill the tank")
ltt = int(input())
lt = (ltt*1.00)

if(ltt < 1):
  print("[] is  an Invalid Input:".format(ltt))
  sys.exit()

print("Enter the distance covered")

diss = int(input())
dis=(diss*1.00)
if(diss<1):
  print("[] is an invalid Input".format(diss))
  sys.exit()

hundred = ((lt/dis)*100)
print("Liters/100KM")
print(round(hundred,2))
miles=(dis * 0.6214)
gallons=(lt*0.2642)
mg=miles/gallons
print("Miles/Gallons")
print(round(mg,2))
