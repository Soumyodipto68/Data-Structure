def max_sub_array(nums):
  max_current = max_global = nums[0]
  for num in nums[1:]:
    max_current=max(num,max_current+num)
    max_global=max(max_global,max_current)
  return max_global

nums=[1,4,7,9,10,11,61]
res=max_sub_array(nums)
print(res)  