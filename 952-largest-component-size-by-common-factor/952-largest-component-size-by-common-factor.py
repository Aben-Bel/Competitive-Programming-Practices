class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def getFactors(n):
            factors = [n]
            for i in range(2,int(sqrt(n))+1):
                if n % i == 0:
                    factors.append(i)
                    factors.append(n//i)
            return factors
        
        root = defaultdict(int)
        rank = defaultdict(int)
        size = 0
        
        def find(a, root, rank):
            if a not in root:
                root[a] = a
                rank[a] = 1
                return a
            
            if root[a] == a:
                return a
            
            node = a
            while node != root[node]:
                node = root[node]
            
            root[a] = node
            
            return node
        
        def union(a, b, root, rank):
            p1 = find(a,root, rank)
            p2 = find(b,root, rank)
            
            if p1 == p2:
                return
            
            if rank[p1] > rank[p2]:
                root[p2] = p1
            elif rank[p1] < rank[p2]:
                root[p1] = p2
            else:
                root[p1] = p2
                rank[p2] += 1

        
        for i in range(len(nums)):
            factors = getFactors(nums[i])
            for j in range(len(factors)):
                union(factors[j], nums[i],root,rank)
        
        
        
        nums = set(nums)
        parents = {}
        m = 0
        
        for key in root:
            if key in nums:
                find(key, root, rank)
                parents[root[key]] = parents.get(root[key], 0) + 1
                m = max(m, parents[root[key]])
        
        
        return m
                
            
        
        
        
        
        