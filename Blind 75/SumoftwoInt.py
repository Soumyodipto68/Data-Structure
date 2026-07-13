def getSum(a,b):
  MASK = 0xFFFFFFFF
  while b != 0:
    a,b = (a^b) & MASK, ((a&b)<<1) & MASK 
  return a & MASK

a=10
b=15
res=getSum(a,b)
print(res)