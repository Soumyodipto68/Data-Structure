"""17.Problem Description"""

"""
To Speed up his composition of generating unpredictable rythms. Blue Bandit wants the list of prime numbers available in a range of numbers.Can you help him out?

Write a python/java program to print all prime numbers in the interval [a,b] (a,b both inclusive).

Note
  . Input 1 should be lesser than Input 2.Both the inputs should be     positive
  . Range must always be greter than zero.
  . If any of the condition mentioned above fails,then display "Provide valid input"
  . use a minimum of one for loop and one while loop

Sample Input 1:
  2
  15 
Sample Output 1:
2 3 5 7 11 13 

"""

a=int(input())
b=int(input())

if(a<=0 or b<=0 or a>=b):
  print("Provide valid Input")
else:
  while(a<=b):
    if(a==2):
      print(a,end=" ")
    elif(a==1):
      a+=1
      continue
    else:
      flag=0
      for i in range(2,a//2+1):
        if(a%i==0):
          flag=1
          break
      if flag==0:
        print(a,end=" ")
    a+=1        