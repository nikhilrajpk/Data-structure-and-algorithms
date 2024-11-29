nums = [6,1,6,5,7,2,6,8,9,6]
print(nums)
i = 0
j = len(nums)-1
target = 6
while i < j:
    if nums[i] == target:
        if nums[j] == target:
            j -= 1
            nums[i], nums[j] = nums[j] , target
    i += 1
print(nums)