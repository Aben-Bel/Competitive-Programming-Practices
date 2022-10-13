# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, leftBound, rightBound):
            if not root:
                return True
            
            if not (leftBound < root.val < rightBound):
                return False
            
            return validate(root.left, leftBound, root.val) and validate(root.right, root.val, rightBound)
        
        return validate(root, float('-inf'), float('inf'))