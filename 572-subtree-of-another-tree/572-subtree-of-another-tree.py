# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def similarRootCase(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            
            return root.val == subRoot.val and similarRootCase(root.left,subRoot.left) and similarRootCase(root.right, subRoot.right) 
        
        if not root:
            return False
        
        if similarRootCase(root,subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)