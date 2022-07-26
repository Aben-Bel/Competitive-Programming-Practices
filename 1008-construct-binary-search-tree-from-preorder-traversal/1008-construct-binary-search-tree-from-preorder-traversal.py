# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i=0
        
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(lower, upper):
            if self.i == len(preorder):
                return
            
            val = preorder[self.i]
            if not (lower < val < upper):
                return
            
            self.i+=1
            root = TreeNode(val)
            root.left = helper(lower,val)
            root.right = helper(val, upper)
            
            return root
        
        return helper(0,10001)
        