# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.isPossible = False
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(root, s):
            if not root:
                return False
            if not root.left and not root.right:
                return s == root.val
            
            return dfs(root.left, s-root.val) or dfs(root.right, s-root.val)
        
        return dfs(root,targetSum)