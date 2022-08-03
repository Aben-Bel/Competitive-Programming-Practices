# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        
        level = 1
        result = []
        max_val = float('-inf')
        while queue:
            size = len(queue)
            _sum = 0
            for _ in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
                _sum += cur.val
            max_val = max(max_val, _sum)
            result.append((_sum, level))
            level+=1
        level = float('inf')
        for s, l in result:
            if s == max_val:
                level = min(l, level)
        return level