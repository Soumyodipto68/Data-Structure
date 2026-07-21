"""10 Problem Description:"""

"""
You are required to implement the following fucntion:
Int Calculate(int m,int n);
The function accepts 2 positive integers 'm' and 'n' as its arguments.You are required to calculate the sum of numbers divisible both by 3 and 5, between 'm' and 'n' both inclusive and return the same.

Note:
0<m<=n

Example
Input:
m : 12
n : 50

Output
90
"""

m=int(input("M:"))
n=int(input("N:"))

def calculate(m,n):
  sum1 = 0
  for i in range(m,n+1,1):
    if i%3 == 0 and i%5 == 0:
      sum1 = sum1+i
  print(sum1) 
calculate(m,n)     