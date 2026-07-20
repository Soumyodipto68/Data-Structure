"""7 Problem Description"""

"""
You are given a function,
void *ReplaceCharacter(Char str[],int n,char ch1,char ch2)

The function accepts a string 'str' of length n and two characters 'ch1' and 'ch2' as its arguments.Implemets and return the string 'str' in such a way that all occurrences of 'ch1' in the original string are replaced by 'ch2' and all occurences of 'ch2' in the original string are replaced by 'ch1'.
"""
"""
Assumption: String Contains only lower case alphabet letters

Note:
Return null if the String is null 
If both characters are not present in the string or both of them are the same, then return the string unchange

Example:
Input:
Str: apples
ch1: a
ch2: p
Output:
paales

"""

def ReplaceCharacter(str1,ch1,ch2):
  result=' '
  if str1 != None:
    result = str1.replace(ch1,"*").replace(ch2,ch1).replace("*",ch2)
    return result
  return "Null"

str1=input("string:")  
ch1=input("ch1:")  
ch2=input("ch2:")  
print(ReplaceCharacter(str1,ch1,ch2))