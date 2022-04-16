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
                
    
    def getResult(self):
        for key in self.root:
            self.find(key)
        
        self.root = (sorted(self.root.items(), key=lambda x: x[1]))
                   
        prev = self.root[0][1]
        bigOutput = []
        output = []
        output.append(self.root[0][0][0])
        
        for (key, val) in self.root:
            if val == prev:
                output.append(key[1])
                
            else:
                prev = val
                bigOutput.append([output[0]] + sorted(output[1:]))
                output = []
                output.extend([key[0], key[1]])
                
        bigOutput.append([output[0]] + sorted(output[1:]))
                
        return (bigOutput)
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        disjoint = DisjointSet()
        for acc in range(len(accounts)):
            for a in range(1, len(accounts[acc])):
                disjoint.union((accounts[acc][0], accounts[acc][1]), (accounts[acc][0], accounts[acc][a]))
        
        return (disjoint.getResult())