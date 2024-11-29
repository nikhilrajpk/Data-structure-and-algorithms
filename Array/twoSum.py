def twoSum(nums, target):
    res_map = set()
    for i in nums:
        if target - i in res_map:
            return [target-i,i]
        else:
            res_map.add(i)
    return "No values."


nums = [6,5,4,8,9,0]
target = 10
print(twoSum(nums, target))