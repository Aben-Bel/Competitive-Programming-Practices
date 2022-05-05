class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        for j in range(len(folder)):
            i=0
            ele = folder[j]
            while i<len(ele)-1:
                if ele[i]!='/' and ele[i+1]=='/':
                    ele = ele[:i+1] + " " + ele[i+1:] 
                    i+=1
                i+=1
            folder[j] = ele
                
        
        for folders in folder:
            self.addFolder(trie, folders)
        result = []
        self.extractFolders(trie, result)
        return result
        
    def addFolder(self, trie, folder):
        node = trie
        for letter in folder.split(" "):
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["*"] = folder
    
    def extractFolders(self, node, result):
        for key in node:
            if "*" in node[key]:
                folder = node[key]["*"]
                folder = folder.replace(" ", "")
                result.append(folder)
            else:
                self.extractFolders(node[key], result)
