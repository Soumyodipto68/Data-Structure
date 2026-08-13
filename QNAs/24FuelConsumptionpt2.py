"""24.Problem Statement"""

"""

Write a Program to calculate the fuel consupmtion of your  ga
truck.The Program should ask the user to enter the quantity of diesel to fill up the tank goes dry.Calculate the fuel 
consupmtion and display it in the format (liters per 100 kilometers)

Convert the same resukt to the US style of miles per gallon
and display the result, If the quantity or distance is zero or 
negetive display "is an Invalid Input"

[Note: The US approach of the fuel consumptio calculate
(distance/fuel) is the inverse of European approach 
(fuel/distance).Also note that 1 kilometer is 0.6214 miles,and 1 liter is 0.2642.]

The result should be with two decimal place. To get two decimal place refer the below-mentioned print statement:
cost=670
print("You need a sum of Rs",cost."to cover the trip")


"""


fuel = float(input("fuel:"))
distance = float(input("distance:"))

if fuel <= 0 or distance <= 0:
    print("Invalid Input")
else:
    liters_per_100km = (fuel / distance) * 100
    print("{:.2f}".format(liters_per_100km))

    miles = distance * 0.6214
    gallons = fuel * 0.2642
    mpg = miles / gallons
    print("{:.2f}".format(mpg))
