def contains_duplicates(nums):
  seen=set()
  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False
nums1 = [41,5,6,9,6,944,58]
res1=contains_duplicates(nums1)
nums2 = [5,1,7,9,91,2,65,96]
res2=contains_duplicates(nums2)
print(res1)
print(res2)