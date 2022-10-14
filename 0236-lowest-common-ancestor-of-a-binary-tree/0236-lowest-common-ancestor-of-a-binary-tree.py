# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(root,p,q):
            if not root:
                return False

            left = dfs(root.left,p,q) 
            right = dfs(root.right,p,q)

            if left and right:
                self.ans = root
            elif root == p and (left or right):
                self.ans = root
            elif root == q and (left or right):
                self.ans = root
            elif root == p or root == q:
                return True
            else:
                return left or right
            
            return True
        dfs(root,p,q)
        return self.ans