# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def getMinimum(root):
            if root.left:
                return getMinimum(root.left)
            return root.val
        
        def getMax(root):
            if root.right:
                return getMax(root.right)
            return root.val
            
        def validate(root, lb, rb):
            if not root:
                return True
            if lb >= root.val or root.val >= rb:
                return False
            
            return validate(root.left, lb,root.val) and validate(root.right, root.val, rb)
        _max = getMax(root)
        _min = getMinimum(root)
        
        return validate(root, _min-1,_max+1)
            
            
        