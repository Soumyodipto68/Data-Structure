def twoSum(nums,target):
  num_map = {}
  for i,num in enumerate(nums):
    complement = target-num
    if complement in num_map:
      return [num_map[complement],i] 
    num_map[num] = i

nums = [1,2,4,6,8,9,10]
target = 9
res=twoSum(nums=nums,target=target) 
print(res)