# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root] 
        parent = {root:root}
        while stack:
            cur = stack.pop()
            if cur.left:
                parent[cur.left] = cur
                stack.append(cur.left)
            if cur.right:
                parent[cur.right] = cur
                stack.append(cur.right)
        
        ancestor = set()
        parentP = parent[p]
        parentQ = parent[q]
        while parentP not in ancestor and parentP != parent[parentP]:
            if parentP == q:
                return q
            ancestor.add(parentP)
            parentP = parent[parentP]
        
        while parentQ not in ancestor and parentQ != parent[parentQ]:
            if parentQ == p:
                return p
            ancestor.add(parentQ)
            parentQ = parent[parentQ]
        
        return parentQ
                
            