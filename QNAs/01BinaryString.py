#1.Problem Descripton:

# The Binary number system only uses two digits, 0 and 1 and the number system can be called binarystring. You are required to implement the following function:
# int OperationsBinaryString(char* str);The funcon accepts a string str as its argument. The string str consists of binary digits separatedwith an alphabet as follows:
# – A denotes AND operation
# – B denotes OR operation
# – C denotes XOR Operation
# You are required to calculate the result of the string str, scanning the string to right taking oneoperation at a time, and return the same.

# Note:
# no order of priorities of operations is required.
# Length of str is odd
# if str is NULL or None.return -1

# Input 
# 1C0C1C1A0B1
# Output
# 1

#------------------------------------------------------------------------

def OperationsBinarayString(str):
  a=int(str[0])
  i=1
  while i<len(str):
    if str[i]=='A':
      a&=int(str[i+1])
    elif str[i]=='B':
      b|=int(str[i+1])
    else: 
      a^=int(str[i+1]) 

    i+=2
    return a
str=input("hii: ")
print(OperationsBinarayString(str))
