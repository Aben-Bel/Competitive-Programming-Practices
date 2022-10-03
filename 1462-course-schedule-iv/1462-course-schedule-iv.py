class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrix = [[False for j in range(numCourses)] for i in range(numCourses)]
        
        for a,b in prerequisites:
            matrix[a][b] = True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for l in range(numCourses):
                    if not matrix[j][l]:
                        matrix[j][l] = matrix[j][i] and matrix[i][l]
        
        ans = []
        for a,b in queries:
            ans.append(matrix[a][b])
            
        
        return ans