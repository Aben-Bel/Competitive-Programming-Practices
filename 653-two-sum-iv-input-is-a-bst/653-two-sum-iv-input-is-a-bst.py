# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.check = set()
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root: 
            return False
        
        if k - root.val in self.check:
            return True
        self.check.add(root.val)
        left = self.findTarget(root.left, k)
        right = self.findTarget(root.right, k)
        
        return left or right