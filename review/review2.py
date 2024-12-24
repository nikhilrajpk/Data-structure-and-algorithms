# def merge(nums):
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums)//2
#     left_array = nums[:mid]
#     right_array = nums[mid:]
#     return join(merge(left_array),merge(right_array))
# def join(left_array,right_array):
#     i=j=0
#     new_array = []
#     while i< len(left_array) and j < len(right_array):
#         if left_array[i] >= right_array[j]:
#             new_array.append(left_array[i])
#             i += 1
#         else:
#             new_array.append(right_array[j])
#             j += 1
#     new_array.extend(left_array[i:])
#     new_array.extend(right_array[j:])
#     return new_array

# nums = [4,3,6,33,55,12,21]
# print(merge(nums))


# from collections import deque
# def palindrome(string):
#     stack = deque()
#     for i in string:
#         stack.append(i)
#     j = len(stack)-1
#     for i in string:
#         if i != stack[j]:
#             return False
#         j -= 1
#     return True

# string = 'MALAYALAM'
# print(palindrome(string))

stones = set("aAAbbbb")
print(stones)