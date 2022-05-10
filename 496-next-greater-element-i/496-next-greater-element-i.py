class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                top = stack.pop()
                hashmap[nums2[top]] = nums2[i]
            stack.append(i)
    
        while stack:
            top = stack.pop()
            hashmap[nums2[top]] = -1
        
        for i in range(len(nums1)):
            nums1[i] = hashmap[nums1[i]]
        
        return nums1
            
                