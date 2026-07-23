"""14.Problem Description"""

"""
FOE College wants to recognize the department which has succeeded in getting the maximum numbers of placements for this academic year. The department thats have participated in the requitment drive are CSE,ECE,MECH. Help the college find the depatment getting maximum placements. Check for all the possible output given in the sample snapshot

Note: if any input is negetive, the output should be "Input is invaild". if all department has equal number of placements the output should be "None of the department has got the highest placement".

Sample Input 1:
  - Enter the no of students placed in CSE:90
  - Enter the no of studnets placed in ECE:45
  - Enter the no of students placed in MCHEH:70

Sample Output 1: 
  - Highest placements 
  CSE
"""

import sys

cse=int(input("Enter the no of students placed in CSE: "))
ece=int(input("Enter the no of students placed in ECE: "))
mech=int(input("Enter the no of students placed in MECH: "))

if (cse<0 or ece<0 or mech <0):
  print("input is invalid")
  sys.exit()
elif(cse==ece and ece==mech):
  print("None of the department has got the highrst placement")
  sys.exit()
print("Highest placement")

m=max(cse,ece,mech)
if(cse==m):
  print("CSE")
if(ece==m):
  print("ECE")
if(mech==m):
  print("MECH")  