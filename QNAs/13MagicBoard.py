"""13.Problem Description"""


"""
Ritik wants a Magic Board,Which displays a characters for a corresponding numbers for his science Project. Help him to develop such an application.

For Example when the digits are 65 66 67 68 are entered, the alphabet  ABCD are to be displayed.[assume the number of inputs should be always 4]

Sample Input 1:
  - Enter the digits:
    65
    66
    67
    68
Sample Output 1:
  65-A
  66-B
  67-C
  68-D     
"""

a=int(input())
b=int(input())
c=int(input())
d=int(input())

print(str(a)+"-"+chr(a))
print(str(b)+"-"+chr(b))
print(str(c)+"-"+chr(c))
print(str(d)+"-"+chr(d))
