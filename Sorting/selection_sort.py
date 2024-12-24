def selection(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

nums = [1,5,7,3,2,32,21]
print(selection(nums))