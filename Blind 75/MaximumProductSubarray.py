def max_product(nums):
  max_prod = min_prod = result = nums[0]
  for num in nums[1:]:
    candidates = (num,num*max_prod,num*min_prod)
    max_prod = max(candidates)
    min_prod = min(candidates)
    result = max(result,max_prod)
  return result
nums = [1,2,3,4,5,6,7,8,9,10]
res=max_product(nums=nums)
print(res)