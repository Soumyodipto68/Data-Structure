def find_min(nums):
  left,right=0,len(nums)-1
  while left < right:
    mid = (left+right)//2
    if nums[mid]>nums[right]:
      left = mid + 1
    else:
      right = mid
  return nums[left]

nums = [1,2,3,4,5,6,7]
res=find_min(nums)
print(res)
