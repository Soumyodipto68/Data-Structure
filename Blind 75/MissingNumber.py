def missingNumber(nums):
  n=len(nums)
  return n*(n+1)//2-sum(nums)

nums=[1,2,4,5,6,7]
res=missingNumber(nums)
print(res)