class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.d = Counter(nums2)
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        key = self.nums2[index]
        self.d[key] -= 1
        if key+val not in self.d:
            self.d[key+val] = 0
        self.d[key+val] += 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        count = 0
        for i in range(len(self.nums1)):
            val = tot - self.nums1[i]
            if val in self.d:
                count += self.d[val]
        
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)