"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        cur = head
        while cur:
            if cur.child:
                nodes = self.flatten(cur.child)
                temp = cur.next
                cur.next = nodes
                nodes.prev = cur
                
                while nodes and nodes.next:
                    nodes = nodes.next
                nodes.next = temp
                if temp:
                    temp.prev = nodes
                cur.child = None
                cur = temp
            else:
                cur = cur.next
            
        return head
        
        