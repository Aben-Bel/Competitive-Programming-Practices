# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def getCount(root):
            if not root:
                return (0,0)

            ln, lc = getCount(root.left)
            rn, rc = getCount(root.right)

            
            c =  lc + rc + 1 - root.val
            self.ans += abs(c)
            return (ln+rn+1, c)
        
        getCount(root)
        return self.ans