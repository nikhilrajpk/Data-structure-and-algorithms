def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left_array = nums[:mid]
    right_array = nums[mid:]
    new_array = join(merge_sort(left_array),merge_sort(right_array))
    return new_array  
def join(left_array,right_array):
    i,j = 0,0
    new_array = []
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            new_array.append(left_array[i])
            i += 1
        else:
            new_array.append(right_array[j])
            j += 1
    if i != len(left_array):
        new_array.extend(left_array[i:])
    if j != len(right_array):
        new_array.extend(right_array[j:])
    return new_array
nums = [41,5,62,38,647,7,7,21]
print(merge_sort(nums))