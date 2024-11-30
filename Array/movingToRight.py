nums = [6,1,6,5,7,2,6,8,9,6]
print(nums)
i = 0
j = len(nums)-1
target = 6                                             # [9, 1, 8, 5, 7, 2, 6, 6, 6, 6]
while i < j:
    if nums[i] == target:
        if nums[j] == target:
            j -= 1
            nums[i], nums[j] = nums[j] , target
    i += 1
print(nums)


nums1 = [6,1,6,5,7,2,6,8,9,6]                            # O(n)T,   O(1)S
print(nums1)
i = 0
count = 0
while i < len(nums1):                                   #[1, 5, 7, 2, 8, 9, 6, 6, 6, 6]
    if nums1[i] != target:
        nums1[count] = nums1[i]
        count += 1
        nums1[i] = target
    i += 1
print(nums1)