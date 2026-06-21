nums = [34,56,78,90,29,30,10,45,1,3]
n = len(nums)
for i in range (n-2, -1, -1):
    
    for j in range (0, i+1):
        if nums[j]>nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)

# in case of a sorted array flagging is used for getting O(n) TC
