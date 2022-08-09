# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # if k==0:
        #     return target
        parent = {}
        
        def populateParent(root):
            if not root: 
                return 
            
            if root.left:
                parent[root.left.val] = root
            if root.right:
                parent[root.right.val] = root
            
            populateParent(root.left)
            populateParent(root.right)
            
        populateParent(root)
        queue = deque()
        queue.append(target)
        visited = set()
        level = 0
        while queue:
            size = len(queue)
            
            if level == k:
                return list(map(lambda x:x.val, queue))
            
            for _ in range(size):
                cur = queue.popleft()
                visited.add(cur)
                if cur.left and cur.left not in visited:
                    queue.append(cur.left)
                if cur.right and cur.right not in visited:
                    queue.append(cur.right)
                
                if cur.val in parent and parent[cur.val] not in visited:
                    queue.append(parent[cur.val])
            level += 1
            
        return []
                