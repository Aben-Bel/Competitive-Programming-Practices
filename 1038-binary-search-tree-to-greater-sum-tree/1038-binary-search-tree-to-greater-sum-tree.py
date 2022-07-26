# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.presum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root: 
            return 
        
        self.bstToGst(root.right)
        self.presum += root.val
        root.val = self.presum
        self.bstToGst(root.left)
        
        return root