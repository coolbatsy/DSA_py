# using .get in dict

nums = [2,5,4,5,6,7,7,7,3,0,9,8]
nums.sort()
hash = {} # a way of storing the dict 

for i in range(1, len(nums)):
    hash[nums[i]] = hash.get(nums[i],0)+1 #.get func eliminates need of conditionals here

print(hash)
