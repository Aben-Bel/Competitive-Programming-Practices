"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        
        res = []
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                cur = queue.popleft()
                temp.append(cur.val)
                for node in cur.children:
                    queue.append(node)
            res.append(temp)
        return res