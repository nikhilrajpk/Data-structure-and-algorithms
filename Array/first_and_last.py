from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    start = findFirst(nums, target)
    end = findLast(nums, target)

    if start <= end and 0 <= start < len(nums) and nums[start] == target:
        return [start, end]
    return [-1, -1]

nums = [5,7,7,8,8,10,11]
target = 8
print(searchRange(nums,target))