class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        
        k = 0
        for i in range(min(len(ver1), len(ver2))):
            v1 = int(ver1[i])
            v2 = int(ver2[i])
            
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            k = i
        k+=1
        
        for i in range(k, len(ver1)):
            v1 = int(ver1[i])
            if v1 != 0:
                return 1
            
        for i in range(k, len(ver2)):
            v2 = int(ver2[i])
            if v2 != 0:
                return -1
        
        return 0
        
        
        
            