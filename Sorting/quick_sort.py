import random
def quick_sort(nums):
    quick_sort_helper(nums,startIdx=0,endIdx=len(nums)-1)
    return nums
def quick_sort_helper(nums,startIdx,endIdx):
    if endIdx <= startIdx:
        return
    # Random pivot selection
    pivotIdx = random.randint(startIdx, endIdx)
    nums[startIdx], nums[pivotIdx] = nums[pivotIdx], nums[startIdx]
    pivotIdx = startIdx
    leftIdx = pivotIdx+1
    rightIdx = endIdx
    while leftIdx<=rightIdx:
        if nums[leftIdx] > nums[pivotIdx] and nums[rightIdx] < nums[pivotIdx]:
            nums[leftIdx], nums[rightIdx] = nums[rightIdx], nums[leftIdx]
            leftIdx += 1
            rightIdx -= 1
        if nums[leftIdx] <= nums[pivotIdx]:
            leftIdx += 1
        if nums[rightIdx] >= nums[pivotIdx]:
            rightIdx -= 1
    nums[pivotIdx], nums[rightIdx] = nums[rightIdx], nums[pivotIdx]
    
    quick_sort_helper(nums,startIdx,rightIdx-1)
    quick_sort_helper(nums,rightIdx+1,endIdx)
    
nums = [10,5,3,2,7,32,21]
print(quick_sort(nums))