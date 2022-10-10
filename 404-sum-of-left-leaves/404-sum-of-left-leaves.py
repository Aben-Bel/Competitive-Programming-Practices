# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        I am thinking of having a global cummulative sum. then everytime, before i traverse my children, i add the value of my left child and call dfs on both left and right. And, the recurssion will handle the rest
        
        """
        def dfs(root, leftChild):
            if not root:
                return 0 
            
            if not root.left and not root.right:
                if leftChild:
                    return root.val
                else:
                    return 0
            
            return dfs(root.left, True) + dfs(root.right, False)
            
        return dfs(root, False)