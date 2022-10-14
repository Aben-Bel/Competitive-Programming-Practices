class Solution:
    def predecessor(self, root):
        node = root.left
        while node and node.right:
            node = node.right
        return node.val if node else -1

    def successor(self, root):
        node = root.right
        while node and node.left:
            node = node.left
        return node.val if node else -1
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                return None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        