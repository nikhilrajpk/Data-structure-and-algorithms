def insertion(nums):
    current = 0
    n = len(nums)
    for i in range(1,n):
        current = nums[i]
        j = i-1
        while j >=0 and nums[j] > current:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = current
    return nums

nums = [1,5,7,3,2,32,21]
print(insertion(nums))