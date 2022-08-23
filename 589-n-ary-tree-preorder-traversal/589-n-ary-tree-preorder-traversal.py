"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        if not root.children:
            return [root.val]
        
        res = [root.val]
        for node in root.children:
            res.extend(self.preorder(node))
        
        return res