class DisjointSet:
    def __init__(self):
        self.rank = {}
        self.root = {}
        
    def find(self, parent):        
        if self.root.get(parent, parent) == parent:
            self.root[parent] = self.root.get(parent, parent)
            return parent
        
        self.root[parent] = self.find(self.root[parent])        
        return self.root[parent]
    
    
    def union(self, node1, node2):  
        node1Root = self.find(node1)
        node2Root = self.find(node2)
        
        self.rank[node1Root] = self.rank.get(node1Root, 1)        
        self.rank[node2Root] = self.rank.get(node2Root, 1)
        
        if node1Root != node2Root:  
            if self.rank[node1Root] >= self.rank[node2Root]:
                self.root[node2Root] = node1Root
                self.rank[node1Root] += self.rank[node2Root] 

            else:
                self.root[node1Root] = node2Root
                self.rank[node2Root] += self.rank[node1Root]     
         
        
    def isConnected(self, node1, node2):
        return self.find(node1) == self.find(node2)  
    
            

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nodeSize = len(points)
        edges = []
        for i in range(nodeSize):
            for j in range(i+1, nodeSize):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((weight, tuple(points[i]), tuple(points[j])))
              
            
        disjoint = DisjointSet()
        edges.sort()
        result = 0
        count = 0
        for edge in edges:
            if not disjoint.isConnected(edge[1], edge[2]):
                disjoint.union(edge[1], edge[2])
                count += 1
                result += edge[0]
                
            if count == nodeSize - 1:
                break
            
            
        return result