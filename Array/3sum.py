def threeSum(nums):                          # -4,-1,-1,0,1,2
    nums.sort()                              #  i  j        k
    res = []                        
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = len(nums)-1
        while j < k:
            total = nums[i] + nums[j] + nums[k]                            # O(n^2)T
            if total > 0:                                                  # O(k)S 
                k -= 1                                      # where k is the number of unique triplets
            elif total < 0:
                j += 1
            else:
                res.append([nums[i],nums[j],nums[k]])
                j += 1
                # if the jth element is equal to the previous then skip it
                while nums[j] == nums[j-1] and j < k:
                    j += 1
    return res

nums = [-1,0,1,2,-1,-4]
print('triplets are : ', threeSum(nums))