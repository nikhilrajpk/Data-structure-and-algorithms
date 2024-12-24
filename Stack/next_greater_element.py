class Solution:
    def linear(self,nums2,key):
        for i in range(len(nums2)):
            if nums2[i] == key:
                return i
        else:
            return -1
    def nextGreaterElement(self, nums1, nums2):
        result = []
        for i in nums1:
            Idx = self.linear(nums2,i)
            for j in range(Idx+1,len(nums2)):
                if nums2[j] > i:
                    result.append(nums2[j])
                    break
            else:
                result.append(-1)
        return result
    
s = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
result = s.nextGreaterElement(nums1,nums2)
print(result)