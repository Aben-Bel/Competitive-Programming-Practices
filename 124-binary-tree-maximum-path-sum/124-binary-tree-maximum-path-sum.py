# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = -10000 # 6
        def pathSum(root):
            if not root:
                return 0
            self.max = max(self.max, root.val)
            if not root.left and not root.right:
                return root.val
            
            leftChild = pathSum(root.left) # 2
            rightChild = pathSum(root.right) # 3
            # ending at me
            self.max = max(self.max, root.val + max(leftChild, rightChild))
            # consider passing through me
            self.max = max(self.max, root.val + leftChild + rightChild)
            
            # considering children
            return max(root.val, root.val + max(leftChild, rightChild)) 

        pathSum(root)
        return self.max