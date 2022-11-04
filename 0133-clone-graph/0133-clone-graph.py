"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node', dictionary = None) -> 'Node':
        if dictionary == None:
            dictionary = {}
            
        if not node:
            return None
        
        if node.val in dictionary:
            return dictionary[node.val]
        
        if not node.neighbors:
            dictionary[node.val] = Node(node.val)
            return dictionary[node.val]
        
        temp = Node(node.val)
        dictionary[node.val] = temp
        for neigh in node.neighbors:
            temp.neighbors.append(self.cloneGraph(neigh, dictionary))
        
        return temp