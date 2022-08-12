# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        if (root1.val != root2.val): return False 
            
        if  (root1.left == None and root2.left == None) or (root1.left and root2.left and root1.left.val == root2.left.val):
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        
        if  (root1.right == None and root2.right == None) or (root1.right and root2.right and root1.right.val == root2.right.val):
            return self.flipEquiv(root1.right, root2.right) and self.flipEquiv(root1.left, root2.left)
        
        return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
            
        