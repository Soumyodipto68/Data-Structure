def product_expect_self(nums):
  length = len(nums)
  answer = [1]*length

  prefix = 1
  for i in range(length):
    answer[i]=prefix
    prefix *= nums[i]
  
  sufix = 1
  for i in range(length-1,-1-1):
    answer[i] = sufix
    sufix *= nums[i] 
  
  return answer

nums = [15,12,1,5,3,9,7]
res = product_expect_self(nums)
print(res)
