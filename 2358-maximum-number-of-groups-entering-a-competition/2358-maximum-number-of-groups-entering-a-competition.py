class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # [10,6,12,7,3,5]
        # [3,5,6,7,10,12]
        # [0,3,8,14,]
        grades.sort()
        # prefix = [0]*len(grades)
        # for i in range(len(grades)):
        #     if i==0:
        #         prefix[i] = grades[i]
        #         continue
        #     prefix[i] = prefix[i-1] + grades[i]
        # prefix = [0] + prefix
        # n = 1
        # prev = 0
        # s = 0
        # count = 1
        # for i in range(len(grades)):
        #     if n - s - i == 0:
        #         val = prefix[i] - prefix[s]
        #         if val == prev:
        #             return count
        #         n+=1
        #         s=i
        #         count+=1
        # return count
        n = 1
        s = 0
        prev = 0
        count = 0
        # [8,8]
        # [1,2,3,4,5]
        while s+n<=len(grades):
            count+=1
            s = s+n
            n += 1
        return count
           