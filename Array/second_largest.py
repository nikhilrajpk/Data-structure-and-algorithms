nums = [41,5,62,38,647,7,7,21]
large = nums[0]
sec_large = nums[1]
for i in range(len(nums)):
    if nums[i] > large:
        sec_large = large
        large = nums[i]
    elif nums[i] > sec_large and nums[i] != large:
        sec_large = nums[i]
print(large,sec_large)