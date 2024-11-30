def twoSum(nums, target):
    res_map = set()
    for i in nums:                                             #  O(n)ST 
        if target - i in res_map:
            return [target-i,i]
        else:
            res_map.add(i)
    return "No values."


def new(nums, target):
    left = 0
    right = len(nums)-1
    nums.sort()                                               #  O(nlogn)
    while left < right:                                       #  O(n)
        if nums[left] + nums[right] == target:              
            return [nums[left],nums[right]]                     #  O(nlogn)T            O(1)S
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return []


nums = [6,5,4,8,9,0]
target = 10
print(twoSum(nums, target))

print('new = ', new(nums,target))