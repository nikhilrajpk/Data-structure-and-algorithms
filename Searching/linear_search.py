"""_summary_
Time complexity : O(n) using the for loop.
Space complexity : O(1) no additional space used so constant space.
"""
def linear_iteration(nums,key):
    for i in range(len(nums)):
        if nums[i] == key:
            return i+1

"""_summary_
Time complexity : O(n) using the recursion.
Space complexity : O(n) because of the call stack frame for the recursion.
"""
def linear_recursion(nums,key,i):
    if nums[i] == key:
        return i+1
    return linear_recursion(nums,key,i+1)
nums = [1,-1,8,10,4]
key = 4
print('element found at the index :',linear_recursion(nums,key,i=0))