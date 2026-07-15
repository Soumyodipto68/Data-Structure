"""5 Problem Statement"""

"""
N-based notation is a system for writing numbers that uses only n different symbols.These symbols are the first n symbols from the given notation list(including the symbol for o)
Decimal to n base notaion are (0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:A,11:B and so upto 35:Z)
"""
"""
Implement the following function 
Char*DectoNBase(int n, int num):
The function accept positive integer n and num Implement the function to calculate the n-baseequivalent of num and return the same as a string
Steps: 
-Divide the decimal number by n,Treat the division as the integer division -Write the the remainder (in n-base notation) 
-Divide the quoent again by n, Treat the division as integer division 
-Repeat step 2 and 3 until the quotient is 0 In The n-base value is the sequence of the remainders from last to first

Assumpton:
1 < n < = 36
Example
Input
n: 12
num: 718
Output
4BA

"""

def DectoNBase(n,num) :
  reminder=[]
  quotient = num//n
  reminder.append(num%n)
  while quotient !=0:
    reminder.append(quotient%n)
    quotient=quotient//n
  reminder=reminder[::-1]
  eqivalent=''
  for i in reminder:
    if n>9:
      a=i-9
      a=64+a
      eqivalent+=chr(a)
    else:
      eqivalent+=str(i)
  return eqivalent


n=int(input("n:"))
num=int(input("num:"))

print(DectoNBase(n,num))