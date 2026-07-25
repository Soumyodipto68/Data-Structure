"""16.Problem Description"""

"""
Reha Pandey's teacher has asked her to prepare well for the lesson on sesasons. When her teacher tells a month, she needs to say the season corresponding to that month,
Write a program to solve the above task.

 . Spring - March to May
 . Summer - June to August
 . Autumn - Sepetember to November
 . Winter - December to February

Month should be in the range 1 to 12. if not the output should be "invalid month"

Sample Input 1:
  .Enter the month:11

Sample output 1:
  .Season:Autumn  

"""

mon=int(input("Enter the number of month(eg. january=1,february=2): "))
if(mon>12):
  print("invalid month")

if(mon==3 or mon==4 or mon==5):
  print("Season:Spring")
elif(mon==6 or mon==7 or mon==8):
  print("Season:Summer")  
elif(mon==9 or mon==10 or mon==11):
  print("Season:Autumn")  
elif(mon==12 or mon==1 or mon==2):
  print("Season:Winter")  