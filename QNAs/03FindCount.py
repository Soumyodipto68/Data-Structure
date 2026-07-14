"""3 Problem Statement"""

"""
You are given a function.
int findCount(int arr[],int length,int num,int diff):
the function accepts an integer array 'arr', its length and two integer variables 'num' and 'diff'.
Implement this fucntion to find and return the number of elements of 'arr' having an absolute difference of less than or equal to 'diff' with 'num'
"""
"""
Note:
In case there is no element in 'arr' whose absolute difference with 'num' is less than or equal to 'diff' return -1
"""
"""
Example:
Input:
arr: 12 3 14 56 77 13
num: 13
diff: 2

Output:
3
"""

def findCount(arr,length,num,diff):
  count=0
  for i in range(length):
    if(abs(arr[i]-num)<=diff):
      count+=1
  if count:
    return count
  return 0

length=int(input("Length:"))  
arr=list(map(int,input("arr:").split()))  
num=int(input("Num:"))  
diff=int(input("Diff:")) 

print(findCount(arr,length,num,diff))