/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int findBottomLeftValue(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int lastElement = 0;
        while(!queue.isEmpty()){
            int size = queue.size();
            boolean last = true;
            while(size>0){
                TreeNode node = queue.remove();
                if(last){
                    last = !last;
                    lastElement = node.val;
                }
                if(node.left!=null)queue.offer(node.left);
                if(node.right!=null) queue.offer(node.right);
                
                size-=1;
            }
        }
        return lastElement;
    }
}