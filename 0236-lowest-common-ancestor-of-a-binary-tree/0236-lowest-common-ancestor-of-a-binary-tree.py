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
        while p not in ancestor:
            ancestor.add(p)
            p = parent[p]
        
        while q not in ancestor:
            ancestor.add(q)
            q = parent[q]
        
        return q
                
            