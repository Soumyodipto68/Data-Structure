"""20.Lucky Numbers"""

"""
Chaman planned to choose a fout digit lucky number for his car.His lucky numbers are 3,5 and 7.Help him find the number, whose sum is divine by 3 or 5 or 7. Provide a valid car number, Fails to provide a valid input then display that number is not a valid car number.

Note-The input other than 4 digit positive number[include negetive and 0] is consider as invalid.

Sample Input 1:
  . Enter the car no:1234
Sample Output 1:
  . Lucky Number

"""

carNum=list(map(int,input("Enter the no of the Car:")))

n=sum(carNum)
if(n%3==0 or n%5==0 or n%7==0):
  print("Lucky Number")
else:
  print("sorry, Not my Lucky number")