# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache(None)
        def dp(node, canRob):
            if not node:
                return 0
            
            
            not_rob = dp(node.left,True) + dp(node.right, True)
            rob = 0
            if canRob:
                rob = dp(node.right,False) + dp(node.left,False) + node.val
            
            return max(rob, not_rob)
        
        return dp(root,True)
        