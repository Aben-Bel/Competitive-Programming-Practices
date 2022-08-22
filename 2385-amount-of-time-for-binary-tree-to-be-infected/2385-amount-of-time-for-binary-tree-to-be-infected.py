
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        self.target = None
        self.count = 0
        
        def dfs(root):
            if not root:
                return 
            if root.val == start:
                self.target = root
            self.count += 1
                
            if root.left:
                parent[root.left.val] = root
            if root.right:
                parent[root.right.val] = root
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        # print(self.target)
        queue = deque()
        queue.append(self.target)
        level = 0
        visited = set()
        while queue:
            size = len(queue)
            if len(visited) == self.count:
                break
            for _ in range(size):
                cur = queue.popleft()
                visited.add(cur)
                if cur.val in parent and parent[cur.val] not in visited:
                    queue.append(parent[cur.val])
                if cur.left and cur.left  not in visited:
                    queue.append(cur.left)
                if cur.right and cur.right not in visited:
                    queue.append(cur.right)
            level += 1
        return level-1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            