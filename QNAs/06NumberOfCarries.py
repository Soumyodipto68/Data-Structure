"""6. Problem Description"""

"""
A Carry is a digit that is transferred to left if sum of digits exceeds 9 while adding two numbers from right to left one digit at a time.
You are required to implement the following fucntion.
int NumberofCarries(int num1,int num2):

the Function accepts two numbers 'num1' and 'num2' as its arguments You are required to calculate and return the total number of carries generated while adding digits of two numbers 'num1' and 'num2'.

"""
"""
Assumption:
num1,num2>=0

Example:
Input
num 1:451
num 2:349

Output:
2
"""

def NumberOfCarries(n1,n2):
  count=0
  carry=0
  if len(n1)<=len(n2):
    l=len(n1)-1
  else:
    l=len(n2)-1
  for i in range(l+1):
    temp=int(n1[l-i])+int(n2[l-i])+carry
    if len(str(temp))>1:
      count+=1
      carry=1
    else:
      carry=0

  return count+carry

n1=(input("n1:"))
n2=(input("n2:"))
print(NumberOfCarries(n1,n2))