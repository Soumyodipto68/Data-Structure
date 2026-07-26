"""18.Problem Description"""

"""
Goutam and Tarul plays by telling numbers. Goutam says a number to Tanul. Tanul should first reverse the number and check if it is same as original. if yes, Tanul should say "palindrome". If bit he should say "Not a Palindrome". If the number is negetive, print "Invalid Input".Help Tanul by wirting a Program
"""

"""
Sample Input 1:
212112

Sample Output 2:
Palindrome

Sample Input 2:
6186

Sample Output 2:
Not a Palindrome

"""

n=input()

if(int(n)<0):
  print("Invalid Input")
elif(n==n[::-1]):
  print("Palindrome")

else:
  print("Not a Plaindrome")

  