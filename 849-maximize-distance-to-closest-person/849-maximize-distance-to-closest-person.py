class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        taken = []
        for i in range(len(seats)):
            if seats[i] == 1:
                taken.append(i)
        m = 1
        for i in range(len(taken)-1):
            if i==0:
                m = max(m, taken[i])
            a = taken[i]
            b = taken[i+1]
            m = max(m, (b-a)//2)
        
        if len(taken)==1:
            a = taken[0]
            m = max(m, len(seats)-a-1, a)
        else:
            a = taken[-1]
            m = max(m, len(seats)-a-1)
        
        return m