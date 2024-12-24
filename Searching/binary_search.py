def binary(nums,key):
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = start + ((end-start)//2)
        if nums[mid] == key:
            return mid+1
        elif key < nums[mid]:
            end = mid-1
        else:
            start = mid+1
    return 'No such element in the list'

def binary_recursion(nums,key,start,end,mid):
    mid = start+((end-start)//2)
    if start > end:
        return 'No element found'
    if nums[mid] == key:
        return mid + 1
    elif key < nums[mid]:
        return binary_recursion(nums,key,start,mid-1,mid)
    else:
        return binary_recursion(nums,key,mid+1,end,mid)

nums=[1,2,3,4,5]
key = 4
start = 0
end = len(nums)-1
mid = 0
print('position at the key found : ',binary_recursion(nums,key,start,end,mid))


"""_summary_
Time complexity: O(logn)
Space complexity: O(1) in Iterative method because no additional space is used.
                  O(logn) in Recursive way because of the call stack used for recursion.
"""