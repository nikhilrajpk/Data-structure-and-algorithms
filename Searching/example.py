def binary(nums,key,left,right):
    mid = left + ((right-left)//2)
    if left > right:
        return -1
    if nums[mid] == key:
        return mid
    elif nums[mid] < key:
        return binary(nums,key,mid+1,right)
    else:
        return binary(nums,key,left,mid-1)
    
    
nums = [1,2,3,4,5,6]
key = 4
print(binary(nums,key,left=0,right=len(nums)))