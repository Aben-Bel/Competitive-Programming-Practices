class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
            first search for the node 
            when i find it, 
                i will return its left child and right child
            otherwise,
                i return null
            
            if as a parent, i recieve left,right child
                first i will make my left child, the right child i recieve
                second, i will iterate through the right child until i find null and then attach the left child 
                finally, i will return null
            otherwise
                i will return null                
        """
        if not root:
            return root
        
        if root.val == key:
            if root.right:
                cur = root.right
                while cur and cur.left!=None:
                    cur = cur.left
                cur.left = root.left
                return root.right
            else:
                return root.left
        
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        
        return root
        
        
        
        
#         if root.val == key:
#             return (root.left, root.right)
        
#         leftLeft, leftRight = self.deleteNode(root.left, key)
#         rightLeft, rightRight = self.deleteNode(root.right, key)
        
#         if leftLeft or leftRight:
            
#         elif rightLeft or rightRight:
            
            
#         return None, None
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        