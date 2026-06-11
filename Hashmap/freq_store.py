# storing frequency of nums in an array in a dict in key value pairs

nums = [3,3,4,5,1,2,3,5,6,3,2,3,7]
frequency_map = dict()
nums.sort() #not necessary to sort the array but I did for cleaner output

for i in range(1, len(nums)):

    if nums[i] in frequency_map:
        frequency_map[nums[i]] += 1

    else:
        frequency_map[nums[i]] = 1

print(frequency_map)