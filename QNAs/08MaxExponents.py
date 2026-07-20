"""8.Problem Description"""

"""
You are Given a Function
int MaxExponents (int a, int b);
You have to find and return the number between 'a' and 'b' (range inclusive on both ends) which has the maximum exponents of 2. 
The algorithm to find the number with the maximum exponents of 2 between the given range
- Loop between 'a' and 'b'.Let the looping variable be 'i'.
-Find the exponents (power) of 2 for each 'i' and store the number with maximum exponents of 2 so far in a variable, let say 'max'.
Return 'Max'.

"""
"""
Assumption: a<b
Note: if two or more numbers in the range have the same exponents of 2, return number.

Example
Input:
7
12
Output:
8
"""

def countExponets(i):
  count=0
  while i%2 == 0 and i!=0:
    count+=1
    i=i//2
  return count

def maxExponents(a,b):
  maximum,number=0,a
  for i in range(a,b):
    temp=countExponets(i)
    if temp > maximum:
      maximum,number=temp,i
    return number

a=int(input("a:"))    
b=int(input("b:"))
print(maxExponents(a,b))    