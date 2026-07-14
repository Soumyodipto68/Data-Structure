def hammingWeight(n):
  count = 0
  while n:
    n&= n-1
    count+=1
  return count

n= 11
res=hammingWeight(n)
print(res)