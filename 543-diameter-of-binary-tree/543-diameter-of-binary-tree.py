# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.m = float('-inf')
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, 0)

            left = dfs(root.left)
            right = dfs(root.right)
            s = max(left) + max(right)
            self.m = max(self.m, s)
            return (max(left)+1, max(right)+1)
        
        dfs(root)
        return self.m