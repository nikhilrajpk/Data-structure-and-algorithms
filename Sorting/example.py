# def quick_sort(nums):
#     quick_sort_helper(nums,startIdx=0,endIdx=len(nums)-1)
#     return nums
# def quick_sort_helper(nums, startIdx, endIdx):
#     if endIdx <= startIdx:
#         return nums
#     pivotIdx = startIdx
#     leftIdx = pivotIdx + 1
#     rightIdx = endIdx
#     while leftIdx <= rightIdx:
#         if nums[leftIdx] > nums[pivotIdx] and nums[rightIdx] < nums[pivotIdx]:
#             nums[leftIdx],nums[rightIdx] = nums[rightIdx],nums[leftIdx]
#             leftIdx += 1
#             rightIdx -= 1
#         if nums[leftIdx] <= nums[pivotIdx]:
#             leftIdx += 1
#         if nums[rightIdx] >= nums[pivotIdx]:
#             rightIdx -= 1
#     nums[pivotIdx],nums[rightIdx] = nums[rightIdx],nums[pivotIdx]
    
#     quick_sort_helper(nums,startIdx,rightIdx-1)
#     quick_sort_helper(nums,rightIdx+1,endIdx)
    
#     return nums

# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums)//2
#     left_array = nums[:mid]
#     right_array = nums[mid:]
#     return join(merge_sort(left_array),merge_sort(right_array))
    
# def join(left_array,right_array):
#     i,j = 0,0
#     new_array = []
#     while i < len(left_array) and j < len(right_array):
#         if left_array[i] <= right_array[j]:
#             new_array.append(left_array[i])
#             i+=1
#         else:
#             new_array.append(right_array[j])
#             j+=1 
#     if i != len(left_array):
#         new_array.extend(left_array[i:])
#     if j != len(right_array):
#         new_array.extend(right_array[j:])
    
#     return new_array

# nums = [41,5,62,38,647,7,7,21]
# print(merge_sort(nums))

import random
class Sorting:
    def bubble(self,nums):
        current = 0
        n = len(nums)-1
        while current < n:
            next = current + 1
            if nums[current] > nums[next]:
                nums[current],nums[next] = nums[next],nums[current]
            current += 1
            if current == n:
                current = 0
                n -= 1
        return nums
    def insertion(self,nums):
        for i in range(1,len(nums)):
            current = nums[i]
            j = i-1
            while j>=0 and nums[j] > current:
                nums[j+1],nums[j] = nums[j],nums[j+1]
                j -= 1
        return nums
    def selection(self,nums):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        return nums
    def quick(self,nums):
        self.quick_helper(nums,0,len(nums)-1)
        return nums
    def quick_helper(self,nums,startIdx,endIdx):
        if endIdx<=startIdx:
            return
        pivotIdx = startIdx
        leftIdx = pivotIdx + 1
        rightIdx = endIdx
        while leftIdx<=rightIdx:
            if nums[leftIdx]>nums[pivotIdx] and nums[rightIdx]<nums[pivotIdx]:
                self.swap(nums,leftIdx,rightIdx)
                leftIdx+= 1
                rightIdx-= 1
            if nums[leftIdx] <= nums[pivotIdx]:
                leftIdx += 1
            if nums[rightIdx] >= nums[pivotIdx]:
                rightIdx -= 1
        self.swap(nums,pivotIdx,rightIdx)
        self.quick_helper(nums,startIdx,rightIdx-1)
        self.quick_helper(nums,rightIdx+1,endIdx)
    def swap(self,nums,left,right):
        nums[left],nums[right] = nums[right],nums[left]
        return
    
    def merge(self,nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left_array = nums[:mid]
        right_array = nums[mid:]
        return self.join(self.merge(left_array),self.merge(right_array))
    def join(self,left_array,right_array):
        i = j = 0
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
        
# s = Sorting()
# nums = [41,5,62,38,647,7,7,21]
# print('bubble   ',s.bubble(nums))
# print('insertion',s.insertion(nums))
# print('selection',s.selection(nums))
# print('quick    ',s.quick(nums))
# print('merge    ',s.merge(nums))