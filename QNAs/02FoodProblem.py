"""2.Problem Descripton:"""


""" The fucntion accepts two positive integers 'r' and 'unit' and a positve integer array 'arr' of size 'n' as its arguments 'r' represent the number of rats present in an area.
'unit' is the amount of food each rat consumes and each ith element of array 'arr' represent the amount of food present in 'i+1' house number, where 0 <= i."""

"""
Note:
Return -1 if the array is Null
Return 0 if the total amount of food from all Houses are not sufficient for all the rats.
compute values lies within the integer range.

"""

"""
Example:
input
r:7
unit:2
n:8
arr: 2,8,3,5,7,4,1,2

output:
4

"""

def calculate(r,unit,arr,n):
  if n == 0:
    return -1
  totalfoodRequired=r*unit
  foodtillNow=0
  house=0
  for house in range(n):
    foodtillNow+=arr[house]
    if foodtillNow >= totalfoodRequired:
      break
  if foodtillNow < totalfoodRequired:
    return 0
    
  return house+1

r=int(input("r:"))  
unit=int(input("unit:"))  
arr=list(map(int,input("arr:").split()))
n=int(input("n:"))
print(calculate(r,unit,arr,n))