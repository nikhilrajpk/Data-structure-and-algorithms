def bubble(nums):
    current = 0
    next = 1
    n = len(nums)-1
    while next < n:
        next = current+1
        if nums[current] > nums[next]:
            nums[current],nums[next] = nums[next],nums[current]
        current += 1
        if next == n:
            n -= 1
            current = 0
            next = 1
    return nums

nums = [1,5,3,2,7,32,21]
print(bubble(nums))