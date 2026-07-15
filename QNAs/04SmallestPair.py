"""4 Problem Statement"""

"""
Implement the Following function
def PrductSmallestPair(sum,arr)
The function accepts an integer sum and an integer array arr of size n.
Implement the fucntion to find find the pair, (arr[j],arr[k]) where j!=k,such that arr[j] and arr[k] are the least two elements of array (arr[j]+arr[k] <= sum) and return the product of element of this pair
"""

"""
Note:
Return -1 if array is empty or if n<2
Return 0, if no such pairs found
All computed values lie within integer range.
"""
"""
Example:
Input
sum:9
Arr:5 2 4 3 9 7 1

Output
2
"""
def ProductSmallestPair(sum1,arr):
  n=len(arr)
  if n < 2:
    return -1
  arr=sorted(arr)
  for i in range(n):
    if arr[i]+arr[i+1] <= sum1:
      return arr[i]*arr[i+1]
      break
    else:
      return 0
sum1 = int(input("Enter the sum: "))
arr = list(map(int,input("Enter the array:").split()))

print(ProductSmallestPair(sum1,arr))

